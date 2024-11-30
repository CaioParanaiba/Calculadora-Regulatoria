from flask import Blueprint, render_template, request, redirect, url_for
from database.models.custo import Resultado
from database.models.subcategoria import SubCategoriaPer
from database.models.empresa import Empresa
import json
import numexpr as ne  # Certifique-se de instalar esta biblioteca

resultado_route = Blueprint('resultado', __name__)

@resultado_route.route('/calcular/<int:empresa_id>', methods=['GET', 'POST'])
def calcular(empresa_id):
    print(f"Metodo da requisicao: {request.method}")
    empresa = Empresa.get(Empresa.id == empresa_id)
    subcategorias_per = SubCategoriaPer.select().where(SubCategoriaPer.empresa == empresa)
    
    if request.method == 'POST':
        print(subcategorias_per)
        for sub in subcategorias_per:
            print(f"Nome: {sub.name}, Descrição: {sub.definicao}")
            try:
                # Parseia o JSON com as variáveis
                variaveis = json.loads(sub.quantidades_json)
                # Avalia a fórmula usando as variáveis
                formula = sub.formula
                formula_resultado = ne.evaluate(formula, local_dict=variaveis)
                
                # Parseia o preço variável
                preco_dict = json.loads(sub.preco_variavel)
                preco = float(next(iter(preco_dict.values()), 0.0))
                
                # Calcula o valor final
                valor_calculado = preco * float(formula_resultado)
                
                # Cria o registro na tabela Resultado
                Resultado.create(
                    empresa=empresa,
                    subcategoria_per=sub,
                    valor_calculado=valor_calculado,
                    detalhes_json=sub.quantidades_json
                )
            except Exception as e:
                # Loga o erro, mas continua o processo
                print(f"Erro ao processar subcategoria {sub.name}: {e}")
                continue

        # Redireciona para a página de resultados
        return redirect(url_for('resultado.listar_resultados', empresa_id=empresa_id))

    # Exibe a página de cálculo para revisão
    return render_template('calcular.html', empresa=empresa, subcategorias=subcategorias_per)




from datetime import datetime

@resultado_route.route('/resultados/<int:empresa_id>', methods=['GET'])
def listar_resultados(empresa_id):
    empresa = Empresa.get(Empresa.id == empresa_id)
    resultados = Resultado.select().where(Resultado.empresa == empresa)

    # Processar resultados e calcular o total
    resultados_processados = []
    total_calculado = 0

    for res in resultados:
        valor_calculado = res.valor_calculado or 0
        resultados_processados.append({
            'subcategoria': res.subcategoria_per.name,
            'descricao': res.subcategoria_per.definicao,
            'valor_calculado': valor_calculado
        })
        total_calculado += valor_calculado

    # Obter a data do cálculo
    data_calculo = datetime.now()

    return render_template(
        'resultados.html',
        empresa=empresa,
        resultados=resultados_processados,
        total_calculado=total_calculado,
        data_calculo=data_calculo
    )







@resultado_route.route('/inserir_variaveis/<int:empresa_id>', methods=['GET', 'POST'])
def inserir_variaveis(empresa_id):
    # Mapeamento de nomes amigáveis
    VARIAVEIS_MAPEADAS = {
        'n_interacoes': 'Número de interações',
        'n_funcionarios': 'Número de funcionários',
        'horas': 'Horas',
        'n_compras': 'Número de compras',
        'horas_dedicas': 'Horas dedicadas',
        'tempo': 'Tempo',
        # Mapeamentos para os nomes de preços
        'custo_de_mao_de_obra': 'Custo de Mão de Obra',
        'investimento': 'Investimento',
        'custo_de_perda_receita': 'Custo de Perda de Receita',
        'valor_da_taxa': 'Valor da Taxa',
        'valor_nominal': 'Valor Nominal',
        'custo_de_capital_anual': 'Custo de Capital Anual',
        'custo_de_compra': 'Custo de Compra',
        'valor_do_imposto': 'Valor do Imposto',
        'valor_da_tarifa': 'Valor da Tarifa',
        'valor_dos_emolumentos': 'Valor dos Emolumentos',
        'valor_das_outorgas': 'Valor das Outorgas',
    }

    empresa = Empresa.get(Empresa.id == empresa_id)
    subcategorias_per = SubCategoriaPer.select().where(SubCategoriaPer.empresa == empresa)

    # Processar subcategorias
    subcategorias_processadas = []
    for sub in subcategorias_per:
        # Carregar quantidades_json
        quantidades = json.loads(sub.quantidades_json)
        
        # Verificar se 'unitaria' está em quantidades
        if 'unitaria' in quantidades:
            # Se for unitária, não incluir variáveis
            variaveis_amigaveis = []
        else:
            # Extrair variáveis técnicas da fórmula
            import re
            variaveis_tecnicas = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', sub.formula)
            # Remover duplicatas
            variaveis_tecnicas = list(set(variaveis_tecnicas))
            # Remover 'unitaria' caso esteja na lista
            variaveis_tecnicas = [var for var in variaveis_tecnicas if var != 'unitaria']

            # Converter para nomes amigáveis
            variaveis_amigaveis = [
                {'tecnico': var, 'amigavel': VARIAVEIS_MAPEADAS.get(var, var)}
                for var in variaveis_tecnicas
            ]

        # Extrair o nome do preço variável
        preco_dict = json.loads(sub.preco_variavel)
        preco_key = next(iter(preco_dict.keys()), 'preco')  # Fallback para 'preco' se não houver chave

        # Converter o nome técnico do preço para um nome amigável
        preco_amigavel = VARIAVEIS_MAPEADAS.get(preco_key, preco_key)

        subcategorias_processadas.append({
            'id': sub.id,
            'name': sub.name,
            'descricao': sub.definicao,
            'variaveis': variaveis_amigaveis,  # Variáveis amigáveis (pode ser lista vazia)
            'preco_tecnico': preco_key,        # Nome técnico do preço
            'preco_amigavel': preco_amigavel,  # Nome amigável do preço
        })

    if request.method == 'POST':
        for sub in subcategorias_per:
            # Atualizar a descrição
            nova_descricao = request.form.get(f'descricao_{sub.id}', '').strip()
            if nova_descricao:
                sub.definicao = nova_descricao

            # Carregar quantidades_json
            quantidades = json.loads(sub.quantidades_json)

            # Verificar se é unitária
            if 'unitaria' in quantidades:
                # Não precisa processar variáveis
                variaveis = quantidades  # Mantém como está
            else:
                # Atualizar variáveis
                variaveis = {}
                # Extrair variáveis da fórmula
                import re
                variaveis_tecnicas = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', sub.formula)
                variaveis_tecnicas = list(set(variaveis_tecnicas))
                variaveis_tecnicas = [var for var in variaveis_tecnicas if var != 'unitaria']

                for var in variaveis_tecnicas:
                    variaveis[var] = float(request.form.get(f'{var}_{sub.id}', 0))

            # Extrair a chave de preco_variavel
            preco_dict = json.loads(sub.preco_variavel)
            preco_key = next(iter(preco_dict.keys()), 'preco')

            # Obter o valor do preço a partir do formulário
            preco_value = float(request.form.get(f'{preco_key}_{sub.id}', 0))

            # Atualizar preco_variavel como um JSON string
            sub.preco_variavel = json.dumps({preco_key: preco_value})

            # Atualizar quantidades_json
            sub.quantidades_json = json.dumps(variaveis)

            # Salvar alterações no banco de dados
            sub.save()

        # Redirecionar para a página de cálculo
        return redirect(url_for('resultado.calcular', empresa_id=empresa_id))

    # Passar as subcategorias processadas para o template
    return render_template('inserir_variaveis.html', empresa=empresa, subcategorias=subcategorias_processadas)
