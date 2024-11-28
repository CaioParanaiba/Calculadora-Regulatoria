from database.database import db
from peewee import CharField, Model

class Categoria(Model):
    name = CharField()

    class Meta:
        database = db
