from peewee import *
from ModeloCurso import Curso
from ModeloProfesor import Profesor
from Utilidades import leerConfiguracion

class ProfesorCurso(Model):
    Id_Profesor = ForeignKeyField(Profesor, on_delete='CASCADE', on_update='CASCADE')
    Id_Curso = ForeignKeyField(Curso, on_delete='CASCADE', on_update='CASCADE')

    class Meta:
        primary_key = CompositeKey('Id_Profesor', 'Id_Curso')
        config = leerConfiguracion()
        database = MySQLDatabase(
            config["db"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"]
        )