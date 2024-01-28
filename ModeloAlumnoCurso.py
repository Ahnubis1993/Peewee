from peewee import *
from ModeloCurso import Curso
from ModeloAlumno import Alumno
from Utilidades import leerConfiguracion

class AlumnoCurso(Model):
    Id_Alumno = ForeignKeyField(Alumno, backref='curso', on_delete='CASCADE', on_update='CASCADE', column_name='Id_Alumno')
    Id_Curso = ForeignKeyField(Curso, backref='alumno', on_delete='CASCADE', on_update='CASCADE', column_name='Id_Curso')

    class Meta:
        primary_key = CompositeKey('Id_Alumno', 'Id_Curso')
        config = leerConfiguracion()
        database = MySQLDatabase(
            config["db"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"]
        )