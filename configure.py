# importa os conjuntos de rotas
from routes.home import home_route
from routes.empresa import empresa_route
from database.database import db
from database.models.empresa import Empresa 

def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(empresa_route, url_prefix='/empresa')


def configure_db():
    db.connect()
    db.create_tables([Empresa])
    