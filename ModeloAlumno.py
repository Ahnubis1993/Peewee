from peewee import *
from Utilidades import leerConfiguracion

class Alumno(Model):
    
    Num_Expediente = PrimaryKeyField()
    Nombre = CharField(null=False)
    Apellidos = CharField(null=False)
    Telefono = CharField(null=False)
    Direccion = CharField(null=False)
    Fecha_Nacimiento = DateField(null=False)
    
    class Meta:
        config = leerConfiguracion()
        database = MySQLDatabase(
            config["db"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"]
        )
        indexes = (
            (('Nombre', 'Apellidos'), True,),
        )