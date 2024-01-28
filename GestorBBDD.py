from peewee import *
from playhouse.migrate import *
from ModeloAlumno import Alumno
from ModeloAlumnoCurso import AlumnoCurso
from ModeloCurso import Curso
from ModeloProfesor import Profesor
from ModeloProfesorCurso import ProfesorCurso
from Utilidades import leerConfiguracion
import pymysql

def crearBBDDSQL():

    """
    Se conecta a la bbdd con SQL mediante la configuracion obtenida en el fichero,
    establece conexion y crea la la bbdd correspodiente, la usa y cierra la conexion

    """

    # Leemos la configuracion estructurada
    config = leerConfiguracion()

    try:

        # Conexion MySQL
        conexion = pymysql.connect(user=config["user"], password=config["password"], host=config["host"], port=config["port"])
        cursor = conexion.cursor()

        # Crear la BBDD con MySQL
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['db']}")
        print(f"Base de datos {config['db']} creada correctamente.")

        # Usar BBDD creada
        cursor.execute(f"USE {config['db']}")

        # Cerramos el cursor y la conexion
        cursor.close()
        conexion.close()
    except OperationalError as e:
        print(f"Error de conexión a la base de datos con pymysql: {e}")


def conectarPeeWee():

    """
    Se conecta a la bbdd con PeeWee mediante la configuracion obtenida en el fichero,
    establece conexion a la BBDD que se creo con MySQL y se conecta

    """

    config = leerConfiguracion()

    try:
        
        db = MySQLDatabase(
            config["db"],
            user=config["user"],
            password=config["password"],
            host=config["host"],
            port=config["port"],
        )

        db.connect()
        print("Conexión establecida correctamente con peewee")
        return db

    except OperationalError as e:
        print(f"Error de conexión a la base de datos con peewee: {e}")
        return None


def crearTablaProfesores(conexion):
    """
    Crea la tabla profesores con una clave primaria autoincrementada
    Se establecen los atributos a not null para que se obligue a su insercion
    y se crea un indice unico para los dni

    :param parametro1: conexion a bbdd
    """

    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Profesores("
                       "Id INT AUTO_INCREMENT PRIMARY KEY,"
                       "Dni VARCHAR(9) NOT NULL,"
                       "Nombre VARCHAR(25) NOT NULL,"
                       "Direccion VARCHAR(25) NOT NULL,"
                       "Telefono VARCHAR(9) NOT NULL)")
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_dni ON Profesores (Dni)")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print("Tabla Profesores no creada correctamente: " + str(e))


def crearTablaAlumnos(conexion):
    """
    FIXME DEPRECATED
    Crea la tabla alumnos con una clave primaria
    Se establecen los atributos a not null para que se obligue a su insercion
    y se crea un indice unico para el numero expediente

    :param parametro1: conexion a bbdd
    """

    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Alumnos("
                       "Num_Expediente INT PRIMARY KEY,"
                       "Nombre VARCHAR(25) NOT NULL,"
                       "Apellidos VARCHAR(25) NOT NULL,"
                       "Telefono VARCHAR(9) NOT NULL,"
                       "Direccion VARCHAR(25) NOT NULL,"
                       # Formato fecha dd/mm/yyyy
                       "Fecha_Nacimiento DATE NOT NULL)"
                       )
        cursor.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS idx_nombre_apellidos ON Alumnos (Nombre, Apellidos)")  # Para asegurarse de que no hay dos alumnos con el mismo nombre y apellidos
        conexion.commit()
        cursor.close()
    except Exception as e:
        print("Tabla Alumnos no creada correctamente: " + str(e))


def crearTablaCursos(conexion):
    """
    Crea la tabla cursos con una clave primaria autoincrementada
    Se establecen los atributos a not null para que se obligue a su insercion

    :param parametro1: conexion a bbdd
    """

    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Cursos("
                       "Codigo INT AUTO_INCREMENT PRIMARY KEY,"
                       "Nombre VARCHAR(25) NOT NULL UNIQUE,"
                       "Descripcion VARCHAR(25) NOT NULL)")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print("Tabla Cursos no creada correctamente: " + str(e))


def crearTablaAlumnosCursos(conexion):
    """
    Crea la tabla alumnos_cursos con 2 columnas de los id de las tablas principales,
    ambas columnas son clave primaria y foranea a la vez, ademas se crea un borrado y modificacion en cascada
    para que cuando se borre un dato de la tabla principal, elimine la relacion

    :param parametro1: conexion a bbdd
    """

    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Alumnos_Cursos("
                       "Num_Expediente INT NOT NULL,"
                       "Id_Curso INT NOT NULL,"
                       "FOREIGN KEY (Num_Expediente) REFERENCES Alumnos(Num_Expediente) ON DELETE CASCADE ON UPDATE CASCADE,"
                       "FOREIGN KEY (Id_Curso) REFERENCES Cursos(Codigo) ON DELETE CASCADE ON UPDATE CASCADE,"
                       "PRIMARY KEY (Num_Expediente,Id_Curso))")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print("Tabla Alumnos_Cursos no creada correctamente: " + str(e))


def crearTablaProfesoresCursos(conexion):
    """
    Crea la tabla profesores_cursos con 2 columnas de los id de las tablas principales,
    ambas columnas son clave primaria y foranea a la vez, ademas se crea un borrado y modificacion en cascada
    para que cuando se borre un dato de la tabla principal, elimine la relacion

    :param parametro1: conexion a bbdd
    """

    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Profesores_Cursos("
                       "Id_Profesor INT NOT NULL,"
                       "Id_Curso INT NOT NULL,"
                       "FOREIGN KEY (Id_Profesor) REFERENCES Profesores(Id) ON DELETE CASCADE ON UPDATE CASCADE,"
                       "FOREIGN KEY (Id_Curso) REFERENCES Cursos(Codigo) ON DELETE CASCADE ON UPDATE CASCADE,"
                       "PRIMARY KEY (Id_Profesor,Id_Curso))")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print("Tabla Profesores_Cursos no creada correctamente: " + str(e))


def crearTablas(db):
    """
    Se unen los metodos de creaciones de tablas para realizarlo desde 1 solo metodo

    :param parametro1: conexion a bbdd
    """

    try:
        #db.drop_tables([Alumno, Curso, Profesor], safe=True)
        db.create_tables([Alumno, Curso, Profesor, ProfesorCurso, AlumnoCurso])
    except OperationalError as e:
        print(f"Error al crear las tablas: {e}")

