from peewee import *
from Utilidades import leerConfiguracion

class Profesor(Model):

    Id = AutoField(primary_key=True)
    Dni = CharField(unique=True)
    Nombre = CharField()
    Direccion = CharField()
    Telefono = CharField()

    class Meta:
        config = leerConfiguracion()
        database = MySQLDatabase(
            config["db"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"]
        )
