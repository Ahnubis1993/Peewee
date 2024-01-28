from peewee import *
from ModeloCurso import Curso
from ModeloProfesor import Profesor
from Utilidades import leerConfiguracion

class ProfesorCurso(Model):
    Id_Profesor = ForeignKeyField(Profesor, backref='curso', on_delete='CASCADE', on_update='CASCADE', column_name='Id_Profesor')
    Id_Curso = ForeignKeyField(Curso, backref='profesor', on_delete='CASCADE', on_update='CASCADE', column_name='Id_Curso')

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