from gestionAlumnos import menuAlumnos
from gestionCursos import menuCursos
from gestionProfesores import menuProfesores
from gestorBBD import conectar


conexionBBDD = conectar()

finMenuPrincipal = False

while(finMenuPrincipal is False):
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
    