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
    except:
        print("Error al conectarse a la base de datos, comprueba la conexion y el fichero ConfiguracionBBDD.txt")


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

def crearTablas(db):
    """
    Se unen los metodos de creaciones de tablas para realizarlo desde 1 solo metodo

    :param parametro1: conexion a bbdd
    """

    try:
        db.create_tables([Alumno, Curso, Profesor, ProfesorCurso, AlumnoCurso])
    except OperationalError as e:
        print(f"Error al crear las tablas: {e}")
    except AttributeError:
        print("No se pudieron crear las tablas debido a un error de conexion")

