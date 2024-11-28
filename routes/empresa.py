from flask import Blueprint, render_template, request
from database.models.empresa import Empresa
import logging

empresa_route = Blueprint('empresa', __name__)

"""
Rota de empresas

- /empresas/ (POST)   - Inserir empresa no servidor
- /empresas/new (GET) - Renderizar o formulario de criar empresa
"""


@empresa_route.route('/', methods=['POST'])
def inserir_empresa():
    """Inserir os dados da empresa no banco de dados"""
    data = request.json
    
    nova_empresa = Empresa.create(
        name=data["name"],
        lei=data["lei"],
    )
    
    return '', 200


@empresa_route.route('/new')
def form_empresa():
    """ formulario para cadastrar um cliente """
    return render_template('form_empresa.html')


