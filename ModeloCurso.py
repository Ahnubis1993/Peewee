from peewee import *
from Utilidades import leerConfiguracion

class Curso(Model):
    Codigo = AutoField(primary_key=True)
    NombreCurso = CharField(unique=True, null=False)
    Descripcion = CharField(null=False)

    class Meta:
        config = leerConfiguracion()
        database = MySQLDatabase(
            config["db"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"]
        )