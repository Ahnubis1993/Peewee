
def leerConfiguracion():
    """
    Lee un fichero por lineas para buscar los datos que se insertan
    en la configuracion del acceso a la bbddd

    :param parametro1: conexion a bbdd
    """

    # Leemos fichero configuracion
    file = open("ConfiguracionBBDD.txt", "r")
    # Leo y cargo las lineas en la variable archivoConfiguracion
    archivoConfiguracion = file.readlines()

    # Inserta y crea las variables para la configuracion de la BBDD (independientemnte del orden en el archivo)
    for linea in archivoConfiguracion:

        lineaDividida = linea.split(":")

        if(lineaDividida[0].strip() == "db"):
            baseDatos = lineaDividida[1].strip()
        elif (lineaDividida[0].strip() == "usuario"):
            usuario = lineaDividida[1].strip()
        elif (lineaDividida[0].strip() == "contrasenia"):
            contrasenia = lineaDividida[1].strip()
        elif (lineaDividida[0].strip() == "host"):
            host = lineaDividida[1].strip()
        elif (lineaDividida[0].strip() == "puerto"):
            puerto = lineaDividida[1].strip()

    # Si alguno de los campos esta vacio se establece su valor por defecto
    if(baseDatos == ""):
        baseDatos = "jorgeGomez_gustavoPlaza_Pewee"
    if (usuario == ""):
        usuario = "root"
    if (contrasenia == ""):
        contrasenia = "alumno"
    if (host == ""):
        host = "localhost"
    if (puerto == ""):
        puerto = "3306"

    config = {
        'db': baseDatos,  # FIXME Placeholder, meter la db en el fichero de config
        'user': usuario,
        'password': contrasenia,
        'host': host,
        'port': int(puerto),
    }

    return config

def confirmacion(mensaje):
    
    """
    Solicita al usuario una confirmacion mediante un mensaje.

    Args:
        mensaje (str): El mensaje que se mostrara al usuario.

    Returns:
        bool: True si la respuesta es afirmativa, False si es negativa.
    """
    
    salir = False
    eleccion = False
    while(not salir):
        respuesta = input(mensaje).strip().lower()
        if(respuesta.startswith("s")):
            eleccion = True
            salir = True
        elif(respuesta.startswith("n")):
            eleccion = False
            salir = True
        else:
            print("Opcion incorrecta")
            
    return eleccion