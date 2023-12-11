from GestionProfesores import busquedaProfesor
from GestionAlumnos import busquedaAlumno
from GestionCursos import busquedaCurso
from Utilidades import confirmacion
from pymysql import IntegrityError


def impartirCurso(conexionBBDD):
    print("-- Asignacion de Curso a Profesor ---")
    idProfesor = busquedaProfesor(conexionBBDD)
    codigoCurso = busquedaCurso(conexionBBDD)
    if(idProfesor != -1 and codigoCurso != -1):
        try:
            # Ejecuto consulta para ver si el curso ya esta asignado, para ello tiene que haber alguna id del curso
            cursor = conexionBBDD.cursor()
            cursor.execute("SELECT * FROM Profesores_Cursos WHERE Id_Curso = %s", (codigoCurso))
            resultado = cursor.fetchone()
            
            # Si ya existe, un profesor lo esta impartiendo
            if(resultado):
                print("El curso ya tiene asignado a un profesor\n")
            # Si no, lo asignamos
            else:
                cursor.execute("INSERT INTO Profesores_Cursos (Id_Profesor, Id_Curso) VALUES (%s, %s)", (idProfesor, codigoCurso))
                conexionBBDD.commit()
                print("El profesor ahora impartira el curso\n")
                
        except IntegrityError:
            print("El profesor ya esta impartiendo ese curso")
        except:
            print("No se ha producido ninguna accion")
        finally:
            if(cursor is not None):
                cursor.close()
    else:
        print("Los resultados de busqueda no encuentran en la base de datos")
    
def dejarImpartirCurso(conexionBBDD):
    print("-- Desasignacion de Curso a Profesor ---")
    idProfesor = busquedaProfesor(conexionBBDD)
    codigoCurso = busquedaCurso(conexionBBDD)
    if(idProfesor != -1 and codigoCurso != -1):
        try:
        # Crear un cursor
            cursor = conexionBBDD.cursor()

            # Consultar si la relación existe antes de intentar borrarla
            cursor.execute("SELECT * FROM Profesores_Cursos WHERE Id_Curso = %s AND Id_Profesor = %s;", (codigoCurso, idProfesor))
            resultado = cursor.fetchone()

            if resultado:
                # Si la relación existe, proceder con el borrado
                cursor.execute("DELETE FROM Profesores_Cursos WHERE Id_Curso = %s AND Id_Profesor = %s;", (codigoCurso, idProfesor))
                conexionBBDD.commit()
                print("Relación borrada correctamente.")
            else:
                print("La relación no existe.")

        except Exception as e:
            print(f"Error al borrar la relación: {e}")
        finally:
            if(cursor is not None):
                cursor.close()
    else:
        print("Los resultados de busqueda no encuentran en la base de datos")
    
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