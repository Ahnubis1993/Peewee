from peewee import *
from Utilidades import leerConfiguracion

class Alumno(Model):
    
    Num_Expediente = PrimaryKeyField()
    Nombre = CharField(max_length=25, null=False)
    Apellidos = CharField(max_length=25, null=False)
    Telefono = CharField(max_length=9, null=False)
    Direccion = CharField(max_length=25, null=False)
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