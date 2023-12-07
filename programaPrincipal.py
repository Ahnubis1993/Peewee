from GestionAlumnos import menuAlumnos
from GestionCursos import menuCursos
from GestionProfesores import menuProfesores
from GestorBBDD import conectar, crearTablas


conexionBBDD = conectar()
crearTablas(conexionBBDD)

finMenuPrincipal = False

while(not finMenuPrincipal):
    print("--- Menu Principal ---")
    print("1 - Gestion Alumnos")
    print("2 - Gestion Profesores")
    print("3 - Gestion Cursos")
    print("0 - Fin Programa")
    opcion = input("Introduce una Opcion: ")
    
    if(opcion=="1"):
        menuAlumnos(conexionBBDD)
    elif(opcion=="2"):
        menuProfesores(conexionBBDD)
    elif(opcion=="3"):
        menuCursos(conexionBBDD)
    elif(opcion=="0"):
        finMenuPrincipal=True
        conexionBBDD.close()
        print("Finalizando Pograma")
    else:
        print("Opcion incorrecta")
    