from flask import Blueprint, render_template, request, redirect, url_for
from database.models.empresa import Empresa

empresa_route = Blueprint('empresa', __name__)

"""
Rota de empresas

- /empresas/ (POST)   - Inserir empresa no servidor
- /empresas/new (GET) - Renderizar o formulario de criar empresa
"""


@empresa_route.route('/', methods=['POST'])
def inserir_empresa():
    """Inserir os dados da empresa no banco de dados"""
    # Receber os dados do formulário
    nome = request.form.get("name")
    lei = request.form.get("lei")

    # Salvar no banco de dados
    nova_empresa = Empresa.create(name=nome, lei=lei)

    # Verificar se foi salvo corretamente e redirecionar
    if nova_empresa.id:
        return redirect(url_for('subcategoria.listar_subcategorias', empresa_id=nova_empresa.id))
    else:
        return "Erro ao salvar a empresa.", 500


@empresa_route.route('/new')
def form_empresa():
    """Formulário para cadastrar uma empresa"""
    return render_template('form_empresa.html')
