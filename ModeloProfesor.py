from peewee import *
from Utilidades import leerConfiguracion

class Profesor(Model):

    Id = AutoField(primary_key=True)
    Dni = CharField(max_length=9, unique=True)
    Nombre = CharField(max_length=25)
    Direccion = CharField(max_length=25)
    Telefono = CharField(max_length=9)

    class Meta:
        config = leerConfiguracion()
        database = MySQLDatabase(
            config["db"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"]
        )
        # La restricción en Dni como campo unico
        constraints = [SQL('UNIQUE (Dni)')]
