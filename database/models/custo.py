from database.database import db
from peewee import Model, ForeignKeyField, FloatField, TextField
from database.models.empresa import Empresa
from database.models.subcategoria import SubCategoriaPer

class Resultado(Model):
    empresa = ForeignKeyField(Empresa, backref="resultados")
    subcategoria_per = ForeignKeyField(SubCategoriaPer, backref="resultados")
    valor_calculado = FloatField(null=True)  # Valor final do cálculo
    detalhes_json = TextField(null=True)  # Informações extras sobre o cálculo (ex: variáveis usadas)

    class Meta:
        database = db