from peewee import *
from Utilidades import leerConfiguracion

class Curso(Model):
    Codigo = AutoField(primary_key=True)
    Nombre = CharField(max_length=25, unique=True, null=False)
    Descripcion = CharField(max_length=25, null=False)

    class Meta:
        config = leerConfiguracion()
        database = MySQLDatabase(
            config["db"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"]
        )