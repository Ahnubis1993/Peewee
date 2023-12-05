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
        
        # Seleccionar la base de datos Concesionario
        conexion.select_db('jorgeGomez_gustavoPlaza')
        print("Conexión establecida correctamente")
        return conexion
     
    except pymysql.Error as e:
        
        print(f"Error de conexión: {e}") 
        return None
    
conectar()