from flask import Blueprint, render_template, request, redirect, url_for
from database.models.subcategoria import SubCategoriaPer, SubCategoria
from database.models.empresa import Empresa  # Importar o modelo Empresa

subcategoria_route = Blueprint('subcategoria', __name__)

@subcategoria_route.route('/<int:empresa_id>')
def listar_subcategorias(empresa_id):
    """
    Exibe a lista de subcategorias disponíveis para vincular a uma empresa específica.
    """
    subcategorias = SubCategoria.select()
    return render_template('listar_subcategoria.html', subcategorias=subcategorias, empresa_id=empresa_id)

@subcategoria_route.route('/duplicar_subcategorias/<int:empresa_id>', methods=['POST'])
def duplicar_subcategorias(empresa_id):
    """
    Duplica as subcategorias selecionadas e as vincula à empresa especificada.
    """
    ids_selecionados = request.form.getlist('subcategoria_id')

    # Recupera a empresa associada
    empresa = Empresa.get(Empresa.id == empresa_id)

    for sub_id in ids_selecionados:
        quantidade = int(request.form.get(f'quantidade_{sub_id}', 1))  # Padrão para 1
        subcategoria = SubCategoria.get(SubCategoria.id == int(sub_id))

        # Criar as duplicações no banco de dados vinculadas à empresa
        for _ in range(quantidade):
            SubCategoriaPer.create(
                name=subcategoria.name,
                categoria=subcategoria.categoria,
                definicao=subcategoria.definicao,
                formula=subcategoria.formula,
                preco_variavel=subcategoria.preco_variavel,
                quantidades_json=subcategoria.quantidades_json,
                empresa=empresa  # Relacionar à empresa
            )

    # Redirecionar de volta para a lista de subcategorias
    return redirect(url_for('resultado.inserir_variaveis', empresa_id=empresa_id))
