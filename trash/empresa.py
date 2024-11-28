from flask import Blueprint, render_template, request
from database.empresa import empresas
from database.models.empresa import Empresa

empresa_route = Blueprint('empresa', __name__)

"""
Rota de empresas

- /empresas/ (POST)              - Inserir empresa no servidor
- /empresas/new (GET)            - Renderizar o formulario de criar empresa
- /empresas/<id> (GET)           - obter os dados da empresa
- /empresas/<id>/edit (GET)      - renderizar um formulário para editar uma empresa
- /empresas/<id>/update (PUT)    - atualizar os dados da empresa    
- /empresas/<id>/delete (DELETE) - deleta a empresa    
"""



@empresa_route.route('/', methods=['POST'])
def inserir_empresa():
    """ inserir os dados da empresa no banco de dados """
    
    data = request.json # Vem do formulário
    
    nova_empresa = Empresa.create(
        name = data["name"],
        lei = data["lei"],
    )
    
    return render_template('form_empresa.html', empresas = nova_empresa)


@empresa_route.route('/new')
def form_empresa():
    """ formulario para cadastrar um cliente """
    return render_template('form_empresa.html')


@empresa_route.route('/<int:empresa_id>')
def detalhe_empresa(empresa_id):
    """ exibir detalhes da empresa """
    return render_template('detalhe_empresa.html')


@empresa_route.route('/<int:empresa_id>/edit')
def form_edit_empresa(empresa_id):
    """ formulario para editar a empresa """
    return render_template('form_empresa.html')


@empresa_route.route('/<int:empresa_id>/update', methods=['PUT'])
def update_empresa(empresa_id):
    """ atualizar informações da empresa """
    pass


@empresa_route.route('/<int:empresa_id>/update', methods=['DELETE'])
def delete_empresa(empresa_id):
    """ deletar informações da empresa """
    pass