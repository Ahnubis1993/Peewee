from GestionAlumnos import menuAlumnos
from GestionCursos import menuCursos
from GestionProfesores import menuProfesores
from GestorBBDD import crearBBDDSQL, crearTablas, conectarPeeWee
from Vinculaciones import menuVinculaciones
from Utilidades import confirmacion

crearBBDDSQL()
db = conectarPeeWee()
crearTablas(db)

finMenuPrincipal = False

while(not finMenuPrincipal):

    """
    Menu Principal donde se gestionan las tablas de la bdd
    Alumnos, profesores y cursos se gestionan en sus correspodientes tablas, mientras que 
    en vinculaciones se realizan las uniones entre tablas de alumnos, profesores y cursos

    """

    print("--- Menu Principal ---")
    print("1 - Gestion Alumnos")
    print("2 - Gestion Profesores")
    print("3 - Gestion Cursos")
    print("4 - Vinculaciones")
    print("0 - Fin Programa")

    # Para capturar el error de interrupcion si salgo del programa sin ejecutar nada (problemas del IDE)
    try:
        opcion = input("Introduce una Opcion: ").strip()
    except KeyboardInterrupt:
        opcion = "0"

    if(opcion=="1"):
        menuAlumnos()
    elif(opcion=="2"):
        menuProfesores()
    elif(opcion=="3"):
        menuCursos()
    elif(opcion=="4"):
        menuVinculaciones()
    elif(opcion=="0"):
        if(confirmacion("Estas seguro que deseas salir del programa? (S/N): ")):
            finMenuPrincipal=True
            db.close()
            print("Finalizando programa")
        else:
            print("Has cancelado la finalzacion del programa")
    else:
        print("Opcion incorrecta")
