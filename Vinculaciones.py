from GestionProfesores import busquedaProfesor
from GestionAlumnos import busquedaAlumno
from GestionCursos import busquedaCurso
from Utilidades import confirmacion
from pymysql import IntegrityError


def impartirCurso(conexionBBDD):
    
    """
    Descripción corta de la función.

    Se realizan las busquedas de los id de curso y profesor para realizar la inserccion
    Luego se hace una consulta para ver si el curso ya existe en la tabla, es decir, si esta siendo impartido,
    y si no esta siendo impartido, se insertan ambos id de curso y profesor en la tabla intermedia

    :param parametro1: conexion a bbdd
    """
    
    print("-- Asignacion de Curso a Profesor ---")
    idProfesor = busquedaProfesor(conexionBBDD)
    codigoCurso = busquedaCurso(conexionBBDD)
    # Si encuentra las busquedas en la bbdd
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
            print("La asignacion no se ha podido efectuar")
        except:
            print("No se ha producido ninguna accion")
        finally:
            if(cursor is not None):
                cursor.close()
    else:
        print("Los resultados de busqueda no encuentran en la base de datos")
    
def dejarImpartirCurso(conexionBBDD):
    
    """
    Descripción corta de la función.

    Se realizan las busquedas de los id de curso y profesor para realizar el borrado
    Luego se hace una consulta para ver si la vinculacion ya existe, y si es asi, se procede a la eliminacion

    :param parametro1: conexion a bbdd
    """
    
    print("-- Desasignacion de Curso a Profesor ---")
    idProfesor = busquedaProfesor(conexionBBDD)
    codigoCurso = busquedaCurso(conexionBBDD)
    if(idProfesor != -1 and codigoCurso != -1):
        try:
        # Crear un cursor
            cursor = conexionBBDD.cursor()

            # Consultar si la relación existe antes de intentar borrarla, si hay un curso en la tabla, ya tiene un profesor asignado
            cursor.execute("SELECT * FROM Profesores_Cursos WHERE Id_Curso = %s AND Id_Profesor = %s;", (codigoCurso, idProfesor))
            resultado = cursor.fetchone()

            if resultado:
                # Si la relación existe, proceder con el borrado
                cursor.execute("DELETE FROM Profesores_Cursos WHERE Id_Curso = %s AND Id_Profesor = %s;", (codigoCurso, idProfesor))
                conexionBBDD.commit()
                print("El profesor ha dejado de impartir el curso.")
            else:
                print("El profesor no esta impartiendo ese curso.")

        except Exception as e:
            print(f"No se ha podido desvincular al profesor el curso: {e}")
        finally:
            if(cursor is not None):
                cursor.close()
    else:
        print("Los resultados de busqueda no encuentran en la base de datos")
    
def matricularAlumno(conexionBBDD):
    
    """
    Descripción corta de la función.

    Se realizan las busquedas de los id de curso y alumno para realizar la inserccion
    Luego se hace una consulta para ver si el curso ya esta matriculado con ese alumno
    y si no es asi, se procede a su matriculacion

    :param parametro1: conexion a bbdd
    """
    
    print("-- Matriculacion Alumno ---")
    numExpediente = busquedaAlumno(conexionBBDD)
    codigoCurso = busquedaCurso(conexionBBDD)
    # Si encuentra las busquedas en la bbdd
    if(numExpediente != -1 and codigoCurso != -1):
        try:
            # Ejecuto consulta para ver si ese curso esta asignado ya al alumno
            cursor = conexionBBDD.cursor()
            cursor.execute("SELECT * FROM Alumnos_Cursos WHERE Id_Curso = %s AND Num_Expediente=%s", (codigoCurso, numExpediente))
            resultado = cursor.fetchone()
            
            # Si ya existe la vinculacion
            if(resultado):
                print("El alumno ya esta matriculado en el curso\n")
            # Si no, lo asignamos
            else:
                cursor.execute("INSERT INTO Alumnos_Cursos (Num_Expediente, Id_Curso) VALUES (%s, %s)", (numExpediente, codigoCurso))
                conexionBBDD.commit()
                print("El Alumno ahora esta matriculado en el curso\n")
                
        except IntegrityError:
            print("La asignacion no se ha podido efectuar")
        except:
            print("No se ha producido ninguna accion")
        finally:
            if(cursor is not None):
                cursor.close()
    else:
        print("Los resultados de busqueda no encuentran en la base de datos")
    
def desmatricularAlumno(conexionBBDD):
    
    """
    Descripción corta de la función.

    Se realizan las busquedas de los id de curso y alumno para realizar el borrado
    Luego se hace una consulta para ver si el curso esta vinculado al alumno,
    y si es asi, se procede a la eliminacion

    :param parametro1: conexion a bbdd
    """

    print("-- Desmatriculacion Alumno ---")
    numExpediente = busquedaAlumno(conexionBBDD)
    codigoCurso = busquedaCurso(conexionBBDD)
    if(numExpediente != -1 and codigoCurso != -1):
        try:
        # Crear un cursor
            cursor = conexionBBDD.cursor()

            # Consulta que verifica que existe la relacion en la tabla Alumnos_Cursos
            cursor.execute("SELECT * FROM Alumnos_Cursos WHERE Id_Curso = %s AND Num_Expediente = %s;", (codigoCurso, numExpediente))
            resultado = cursor.fetchone()

            if resultado:
                # Si la relación existe, proceder con el borrado
                cursor.execute("DELETE FROM Alumnos_Cursos WHERE Id_Curso = %s AND Num_Expediente = %s;", (codigoCurso, numExpediente))
                conexionBBDD.commit()
                print("Alumno desmatriculado correctamente.")
            else:
                print("El alumno no esta matriculado en ese curso.")

        except Exception as e:
            print(f"No se ha podido desmatricular al alumno del curso: {e}")
        finally:
            if(cursor is not None):
                cursor.close()
    else:
        print("Los resultados de busqueda no encuentran en la base de datos")
        
def mostrarRelacionesAlumnos(conexionBBDD):
    print("--- Mostrar Matriculaciones Alumnos ---")
    
    """
    Descripción corta de la función.

    Se realiza una consulta multitabla entre alumnos y cursos y mostrar los datos de la uniones

    :param parametro1: conexion a bbdd
    """
    
    try:
        cursor = conexionBBDD.cursor()
        # Group_Concat, concatena todos los cursos de ese alumno
        cursor.execute("SELECT Alumnos.Num_Expediente, Alumnos.Nombre, Alumnos.Apellidos, Alumnos.Telefono, "
                       "Alumnos.Direccion, Alumnos.Fecha_Nacimiento, GROUP_CONCAT(Cursos.Nombre) AS Cursos "
                       "FROM Alumnos_Cursos, Cursos, Alumnos "
                       "WHERE Alumnos.Num_Expediente = Alumnos_Cursos.Num_Expediente "
                       "AND Cursos.Codigo = Alumnos_Cursos.Id_Curso"
                       "GROUP BY Alumnos.Num_Expediente")
        filas = cursor.fetchall()
        
        if(filas):
            for f in filas:
                idAlu = f[0]
                if(f[0]):
                    print("Alumno:", f[0])
                    print("Nombre:", f[1])
                    print("Apellidos:", f[2])
                    print("Teléfono:", f[3])
                    print("Dirección:", f[4])
                    print("Fecha de Nacimiento:", f[5])
                    print("Curso:", f[6])
                    print("\n")
        else:
            print("No hay alumnos matriculados en cursos")
                
        
    except Exception as e:
        print(f"No se han podido mostrar los datos: {e}")
    
def mostrarRelacionesProfesores(conexionBBDD):
    print("--- Mostrar Asignaciones Profesor ---")

    """
    Descripción corta de la función.

    Se realiza una consulta multitabla entre profesores y cursos y mostrar los datos de la uniones

    :param parametro1: conexion a bbdd
    """
    
    try:
        cursor = conexionBBDD.cursor()
        cursor.execute("SELECT Profesores.Id, Profesores.Dni, Profesores.Nombre, Profesores.Direccion, Profesores.Telefono, "
                       "Cursos.Nombre AS Curso "
                       "FROM Profesores_Cursos, Cursos, Profesores "
                       "WHERE Profesores.Id = Profesores_Cursos.Id_Profesor "
                       "AND Cursos.Codigo = Profesores_Cursos.Id_Curso")
        filas = cursor.fetchall()
        
        if(filas):
            for f in filas:
                print("Profesor:", f[0])
                print("Dni:", f[1])
                print("Nombre:", f[2])
                print("Direccion:", f[3])
                print("Telefono:", f[4])
                print("Curso:", f[5])
                print("\n")
        else:
            print("No ha profesores asignados a cursos")        
        
        
    except Exception as e:
        print(f"No se han podido mostrar los datos: {e}")

def menuVinculaciones(conexionBBDD):
    

    """
    Descripción corta de la función.

    Menu vinculaciones para elegir una de las gestion mediante la insercion de un numero

    :param parametro1: conexion a bbdd
    """
    
    finMenuVinculaciones = False
    
    while(not finMenuVinculaciones):  
        print("--- Menu Vinculaciones ---")
        print("Elige una de las siguientes opciones")
        print("1 - Asignar curso a profesor")
        print("2 - Desasignar curso a profesor")
        print("3 - Matriculacion alumno")
        print("4 - Desmatriculacion alumno")
        print("5 - Mostrar matriculaciones alumnos")
        print("6 - Mostrar asignaciones profesores")
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
        elif(opcion=="5"):
            mostrarRelacionesAlumnos(conexionBBDD)
        elif(opcion=="6"):
            mostrarRelacionesProfesores(conexionBBDD)
        elif(opcion=="0"):
            finMenuVinculaciones = True
            print("Regresando a Menu Principal. Fin Menu Vinculaciones")
        else:
            print("Opcion no valida")