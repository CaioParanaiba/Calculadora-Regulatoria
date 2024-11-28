from flask import Blueprint, render_template, request, redirect, url_for
from database.models.custo import Resultado
from database.models.subcategoria import SubCategoriaPer
from database.models.empresa import Empresa

resultado_route = Blueprint('resultado', __name__)




@resultado_route.route('/calcular/<int:empresa_id>', methods=['GET', 'POST'])
def calcular(empresa_id):
    print(f"Metodo da requisicao: {request.method}")
    """
    Processa os cálculos das subcategorias vinculadas a uma empresa
    e salva os resultados na tabela Resultado.
    """
    # Obtém a empresa pelo ID
    empresa = Empresa.get(Empresa.id == empresa_id)
    
    # Seleciona todas as subcategorias vinculadas à empresa
    subcategorias_per = SubCategoriaPer.select().where(SubCategoriaPer.empresa == empresa)
    # Processa os cálculos ao enviar o formulário
    if request.method == 'POST':
        print(subcategorias_per)
        for sub in subcategorias_per:
            print(f"Nome: {sub.name}, Descrição: {sub.definicao}")
            try:
                # Avalia o JSON com as variáveis
                variaveis = eval(sub.quantidades_json)  # Exemplo: {'n_funcionarios': 10, 'horas': 5}
                # Avalia a fórmula usando as variáveis
                formula_resultado = eval(sub.formula, {}, variaveis)
                
                # Calcula o valor final
                preco = float(sub.preco_variavel or 0)
                valor_calculado = preco * formula_resultado

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
    subcategorias_processadas = [
        {
            'name': sub.name,
            'descricao': sub.definicao or "Descrição não disponível"  # Fallback para evitar None
        }
        for sub in subcategorias_per
    ]

    print(subcategorias_processadas)  # Debug para validar os dados

    # Exibe a página de cálculo para revisão
    return render_template('calcular.html', empresa=empresa, subcategorias=subcategorias_per)




@resultado_route.route('/resultados/<int:empresa_id>', methods=['GET'])
def listar_resultados(empresa_id):
    """
    Exibe os resultados dos cálculos vinculados a uma empresa.
    """
    empresa = Empresa.get(Empresa.id == empresa_id)
    resultados = Resultado.select().where(Resultado.empresa == empresa)

    resultados_processados = [
        {
            'subcategoria': res.subcategoria_per.name,
            'descricao': res.subcategoria_per.definicao,
            'valor_calculado': res.valor_calculado
        }
        for res in resultados
    ]

    return render_template('resultados.html', empresa=empresa, resultados=resultados_processados)






@resultado_route.route('/inserir_variaveis/<int:empresa_id>', methods=['GET', 'POST'])
def inserir_variaveis(empresa_id):
    # Mapeamento de nomes amigáveis
    VARIAVEIS_MAPEADAS = {
        'custo_mao_obra': 'Custo de mão de obra',
        'n_funcionarios': 'Número de funcionários',
        'horas': 'Horas',
        'n_interacoes': 'Número de interações',
        'n_compras': 'Número de compras',
        'horas_dedicas': 'Horas dedicadas',
    }

    empresa = Empresa.get(Empresa.id == empresa_id)
    subcategorias_per = SubCategoriaPer.select().where(SubCategoriaPer.empresa == empresa)

    # Processar subcategorias
    subcategorias_processadas = []
    for sub in subcategorias_per:
        # Extrair variáveis técnicas da fórmula
        variaveis_tecnicas = list(set(sub.formula.replace('*', ' ').split()))

        # Converter para nomes amigáveis
        variaveis_amigaveis = [
            {'tecnico': var, 'amigavel': VARIAVEIS_MAPEADAS.get(var, var)}
            for var in variaveis_tecnicas
        ]

        subcategorias_processadas.append({
            'id': sub.id,
            'name': sub.name,
            'descricao': sub.definicao,
            'variaveis': variaveis_amigaveis,  # Variáveis amigáveis
        })

    if request.method == 'POST':
        for sub in subcategorias_per:
            # Atualizar a descrição
            nova_descricao = request.form.get(f'descricao_{sub.id}', '').strip()
            if nova_descricao:  # Apenas atualiza se não estiver vazio
                sub.definicao = nova_descricao

            # Atualizar variáveis
            variaveis = {}
            for var in sub.formula.replace('*', ' ').split():
                variaveis[var] = float(request.form.get(f'{var}_{sub.id}', 0))

            # Atualizar preço
            preco = float(request.form.get(f'preco_{sub.id}', 0))
            sub.quantidades_json = str(variaveis)
            sub.preco_variavel = preco

            # Salvar alterações no banco de dados
            sub.save()

        # Redirecionar para a página de cálculo
        return redirect(url_for('resultado.calcular', empresa_id=empresa_id))

    # Passar as subcategorias processadas para o template
    return render_template('inserir_variaveis.html', empresa=empresa, subcategorias=subcategorias_processadas)
