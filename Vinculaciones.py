from GestionProfesores import busquedaProfesor
from GestionAlumnos import busquedaAlumno
from GestionCursos import busquedaCurso
from Utilidades import confirmacion
from pymysql import IntegrityError


def impartirCurso(conexionBBDD):
    print("-- Asignacion de Curso a Profesor ---")
    idProfesor = busquedaProfesor(conexionBBDD)
    codigoCurso = busquedaCurso(conexionBBDD)
    try:
        cursor = conexionBBDD.cursor()
        cursor.execute("INSERT INTO Profesores_Cursos (Id_Profesor, Id_Curso) VALUES (%s, %s)", (idProfesor, codigoCurso))
        conexionBBDD.commit()
        print("El profesor ahora impartira el curso")
    except IntegrityError:
        print("El profesor ya esta impartiendo ese curso")
    except:
        print("No se ha producido ninguna accion")
    finally:
        if(cursor is not None):
            cursor.close()
    
def dejarImpartirCurso(conexionBBDD):
    print("-- Desasignacion de Curso a Profesor ---")
    idProfesor = busquedaProfesor(conexionBBDD)
    codigoCurso = busquedaCurso(conexionBBDD)
    try:
        cursor = conexionBBDD.cursor()
        cursor.execute("DELETE FROM Profesores_Cursos WHERE Id_Profesor = %s AND Id_Curso = %s",(idProfesor, codigoCurso))
        conexionBBDD.commit()
        print("El profesor ya no impartira ese curso")
    except IntegrityError:
        print("El profesor no estaba impartiendo ese curso")
    except:
        print("No se ha producido ninguna accion")
    finally:
        if(cursor is not None):
            cursor.close()
    
def matricularAlumno(conexionBBDD):
    print("")
    
def desmatricularAlumno(conexionBBDD):
    print("")

def menuVinculaciones(conexionBBDD):
    
    finMenuVinculaciones = False
    
    while(not finMenuVinculaciones):  
        print("--- Menu Vinculaciones ---")
        print("Elige una de las siguientes opciones")
        print("1 - Asignar curso a profesor")
        print("2 - Desasignar curso a profesor")
        print("3 - Matriculacion alumno")
        print("4 - Desmatriculacion alumno")
        print("0 - Salir")
        opcion = input("Introduce opcion: ").strip()

        if(opcion=="1"):
            impartirCurso(conexionBBDD)
        elif(opcion=="2"):
            dejarImpartirCurso(conexionBBDD)
        elif(opcion=="3"):
            matricularAlumno(conexionBBDD)
        elif(opcion=="4"):
            desmatricularAlumno(conexionBBDD)
        elif(opcion=="0"):
            finMenuVinculaciones = True
            print("Regresando a Menu Principal. Fin Menu Vinculaciones")
        else:
            print("Opcion no valida")