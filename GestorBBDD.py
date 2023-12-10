import pymysql

def leerConfiguracion():
    # Leemos fichero configuracion    
    file = open("ConfiguracionBBDD.txt","r")
    # Leo y cargo las lineas en la variable archivoConfiguracion
    archivoConfiguracion = file.readlines()
    
    # Inserta y crea las variables para la configuracion de la BBDD (independientemnte del orden en el archivo)
    for linea in archivoConfiguracion:
        
        lineaDividida = linea.split(":")
        
        if(lineaDividida[0].strip()=="usuario"):
            usuario=lineaDividida[1].strip()
        elif(lineaDividida[0].strip()=="contrasenia"):
            contrasenia=lineaDividida[1].strip()
        elif(lineaDividida[0].strip()=="host"):
            host=lineaDividida[1].strip()
        elif(lineaDividida[0].strip()=="puerto"):
            puerto=lineaDividida[1].strip()
            
    # Si alguno de los campos esta vacio se establece su valor por defecto
    if(usuario == ""):
        usuario = "root"
    if(contrasenia == ""):
        contrasenia = "alumno"
    if(host == ""):
        host = "localhost"
    if(puerto == ""):
        puerto = "3306"
    
    config = {
    'user': usuario,
    'password': contrasenia,
    'host': host,
    'port': int(puerto),
    } 

    return config
          
def conectar():
    
    # Leemos la configuracion estructurada
    config = leerConfiguracion()
    
    try:
        
        # Creamos conexion y accedemos a la configuracion proporcionada arriba
        conexion = pymysql.connect(**config)
        cursor = conexion.cursor()
        # Si la base de datos no existe, crearla
        cursor.execute("CREATE DATABASE IF NOT EXISTS jorgeGomez_gustavoPlaza")
        
        # Seleccionar la base de datos
        conexion.select_db('jorgeGomez_gustavoPlaza')
        print("Conexión establecida correctamente")
        return conexion
     
    except pymysql.Error as e:
        
        print(f"Error de conexión: {e}") 
        return None
    
def crearTablaProfesores(conexion):
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
        print("Tabla Profesores no creada correctamente: "+str(e))
    
def crearTablaAlumnos(conexion):
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
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_nombre_apellidos ON Alumnos (Nombre, Apellidos)")#Para asegurarse de que no hay dos alumnos con el mismo nombre y apellidos
        conexion.commit()
        cursor.close()
    except Exception as e:
        print("Tabla Alumnos no creada correctamente: "+str(e))
    
def crearTablaCursos(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Cursos("
            "Codigo INT AUTO_INCREMENT PRIMARY KEY," 
            "Nombre VARCHAR(25) NOT NULL,"
            "Descripcion VARCHAR(25) NOT NULL)")
        conexion.commit()
        cursor.close() 
    except Exception as e:
        print("Tabla Cursos no creada correctamente: "+str(e))
        
def crearTablaAlumnosCursos(conexion):
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
        


def crearTablas(conexion):
    crearTablaAlumnos(conexion)
    crearTablaProfesores(conexion)
    crearTablaCursos(conexion)
    crearTablaAlumnosCursos(conexion)
    crearTablaProfesoresCursos(conexion)