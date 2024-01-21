from peewee import *
from GestorBBDD import leerConfiguracion

class Alumno(Model):
    #Campos
    class Meta:
        config = leerConfiguracion()
        database = MySQLDatabase(config["db"], user = config["user"], password = config["password"], host = config["host"], port = config["port"])