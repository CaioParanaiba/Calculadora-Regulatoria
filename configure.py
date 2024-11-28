# importa os conjuntos de rotas
from routes.home import home_route
from routes.empresa import empresa_route
from routes.subcategoria import subcategoria_route
from routes.resultado import resultado_route
from database.database import db
from database.models.empresa import Empresa 
from database.models.custo import Resultado
from database.models.subcategoria import SubCategoria, SubCategoriaPer, valores_iniciais

def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(empresa_route, url_prefix='/empresa')
    app.register_blueprint(subcategoria_route, url_prefix='/subcategoria')
    app.register_blueprint(resultado_route, url_prefix='/resultado')


def configure_db():
    db.connect()
    db.create_tables([Empresa, SubCategoria, SubCategoriaPer, Resultado])
    if SubCategoria.select().count() == 0:
        for valor in valores_iniciais:
            SubCategoria.create(**valor)
    