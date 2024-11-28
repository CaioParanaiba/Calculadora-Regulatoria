from database.database import db
from peewee import CharField, Model, DateTimeField, AutoField
import datetime

class Empresa(Model):
    id = AutoField()
    name = CharField(100)
    lei = CharField()
    date = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db