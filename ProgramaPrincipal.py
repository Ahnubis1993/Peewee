from GestionAlumnos import menuAlumnos
from GestionCursos import menuCursos
from GestionProfesores import menuProfesores
from GestorBBDD import conectar, crearTablas
from Vinculaciones import menuVinculaciones
from Utilidades import confirmacion


db = conectar()
crearTablas(db)

finMenuPrincipal = False

while(not finMenuPrincipal):
    
    """
    Menu Principal donde se gestionan las tablas de la bdd
    Alumnos, profesores y cursos se gestionan en sus correspodientes tablas, mientras que 
    en vinculaciones se realizan las uniones entre tablas de alumnos, profesores y cursos

    :param parametro1: conexion a bbdd
    """
    
    print("--- Menu Principal ---")
    print("1 - Gestion Alumnos")
    print("2 - Gestion Profesores")
    print("3 - Gestion Cursos")
    print("4 - Vinculaciones")
    print("0 - Fin Programa")
    opcion = input("Introduce una Opcion: ")
    
    if(opcion=="1"):
        menuAlumnos(db)
    elif(opcion=="2"):
        menuProfesores(db)
    elif(opcion=="3"):
        menuCursos(db)
    elif(opcion=="4"):
        menuVinculaciones(db)
    elif(opcion=="0"):
        if(confirmacion("Estas seguro que deseas salir del programa? (S/N): ")):
            finMenuPrincipal=True
            db.close()
            print("Finalizando programa")
        else:
            print("Has cancelado la finalzacion del programa")      
    else:
        print("Opcion incorrecta")
    