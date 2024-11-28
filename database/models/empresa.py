from database.database import db
from peewee import CharField, Model, DateTimeField
import datetime

class Empresa(Model):
    name = CharField(100)
    lei = CharField()
    date = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db