from GestionProfesores import busquedaProfesor
from GestionAlumnos import busquedaAlumno
from GestionCursos import busquedaCurso
from ModeloAlumno import Alumno
from ModeloCurso import Curso
from ModeloProfesor import Profesor
from Utilidades import confirmacion
from pymysql import IntegrityError
from ModeloProfesorCurso import ProfesorCurso
from ModeloAlumnoCurso import AlumnoCurso


def impartirCurso():
    
    """
    Se realizan las busquedas de los id de curso y profesor para realizar la inserccion
    Luego se hace una consulta para ver si el curso ya existe en la tabla, es decir, si esta siendo impartido,
    y si no esta siendo impartido, se insertan ambos id de curso y profesor en la tabla intermedia
    """
    
    print("-- Asignacion de Curso a Profesor ---")
    idProfesor = busquedaProfesor()
    codigoCurso = busquedaCurso()
    # Si encuentra las busquedas en la bbdd
    if(idProfesor != -1 and codigoCurso != -1):
        try:
            # Ejecuto consulta para ver si el curso ya esta asignado, para ello tiene que haber algun id del curso
            resultado = ProfesorCurso.get_or_none(Id_Curso=codigoCurso, Id_Profesor=idProfesor)
            # Si ya existe, un profesor lo esta impartiendo
            if(resultado):
                print("El curso ya tiene asignado a un profesor\n")
            # Si no, lo asignamos
            else:
                ProfesorCurso.create(Id_Profesor=idProfesor, Id_Curso=codigoCurso)
                print("El profesor ahora impartira el curso\n")
                
        except IntegrityError:
            print("La asignacion no se ha podido efectuar")
        except:
            print("No se ha producido ninguna accion")
    else:
        print("Los resultados de busqueda no encuentran en la base de datos\n")
    
def dejarImpartirCurso():
    
    """
    Se realizan las busquedas de los id de curso y profesor para realizar el borrado
    Luego se hace una consulta para ver si la vinculacion ya existe, y si es asi, se procede a la eliminacion
    """
    
    print("-- Desasignacion de Curso a Profesor ---")
    idProfesor = busquedaProfesor()
    codigoCurso = busquedaCurso()
    if(idProfesor != -1 and codigoCurso != -1):
        try:
            # Consultar si la relación existe antes de intentar borrarla, si hay un curso en la tabla, ya tiene un profesor asignado
            relacion = ProfesorCurso.get_or_none(Id_Profesor=idProfesor, Id_Curso=codigoCurso)

            if relacion:
                # Si la relación existe, proceder con el borrado
                relacion.delete_instance()
                print("El profesor ha dejado de impartir el curso.")
            else:
                print("El profesor no esta impartiendo ese curso.")

        except Exception as e:
            print(f"No se ha podido desvincular al profesor el curso: {e}")
    else:
        print("Los resultados de busqueda no encuentran en la base de datos\n")
    
def matricularAlumno():
    
    """
    Se realizan las busquedas de los id de curso y alumno para realizar la inserccion
    Luego se hace una consulta para ver si el curso ya esta matriculado con ese alumno
    y si no es asi, se procede a su matriculacion
    """
    
    print("-- Matriculacion Alumno ---")
    numExpediente = busquedaAlumno()
    codigoCurso = busquedaCurso()
    # Si encuentra las busquedas en la bbdd
    if(numExpediente != -1 and codigoCurso != -1):
        try:
            # Ejecuto consulta para ver si ese curso esta asignado ya al alumno
            resultado = AlumnoCurso.get_or_none(Id_Curso=codigoCurso, Id_Alumno=numExpediente)
            # Si ya existe la vinculacion
            if(resultado):
                print("El alumno ya esta matriculado en el curso\n")
            # Si no, lo asignamos
            else:
                AlumnoCurso.create(Id_Alumno=numExpediente, Id_Curso=codigoCurso)
                print("El Alumno ahora esta matriculado en el curso\n")
                
        except IntegrityError:
            print("La asignacion no se ha podido efectuar")
        except:
            print("No se ha producido ninguna accion")
    else:
        print("Los resultados de busqueda no encuentran en la base de datos\n")
    
def desmatricularAlumno():
    
    """
    Se realizan las busquedas de los id de curso y alumno para realizar el borrado
    Luego se hace una consulta para ver si el curso esta vinculado al alumno,
    y si es asi, se procede a la eliminacion
    """

    print("-- Desmatriculacion Alumno ---")
    numExpediente = busquedaAlumno()
    codigoCurso = busquedaCurso()
    if(numExpediente != -1 and codigoCurso != -1):
        try:
            # Consulta que verifica que existe la relacion en la tabla Alumnos_Cursos
            resultado = AlumnoCurso.get_or_none(Id_Alumno=numExpediente, Id_Curso=codigoCurso)

            if resultado:
                # Si la relación existe, proceder con el borrado
                resultado.delete_instance()
                print("Alumno desmatriculado correctamente.")
            else:
                print("El alumno no esta matriculado en ese curso.")

        except Exception as e:
            print(f"No se ha podido desmatricular al alumno del curso: {e}")
    else:
        print("Los resultados de busqueda no encuentran en la base de datos\n")
        
def mostrarRelacionesAlumnos():
    print("--- Mostrar Matriculaciones Alumnos ---")
    
    """
    Se realiza una consulta multitabla entre alumnos y cursos y mostrar los datos de la uniones
    """
    
    try:

        relaciones = (Alumno
                      .select(Alumno, Curso)
                      .join(AlumnoCurso)
                      .join(Curso)
                      .distinct())
        
        if(relaciones):
            for relacion in relaciones:
                print("Num_Expediente:", relacion.Num_Expediente)
                print("Nombre Alumno:", relacion.Nombre)
                print("Apellidos Alumno:", relacion.Apellidos)
                print("Teléfono Alumno:", relacion.Telefono)
                print("Dirección Alumno:", relacion.Direccion)
                print("Fecha de Nacimiento Alumno:", relacion.Fecha_Nacimiento)
                print("Curso:", relacion.Nombre, "\n")
        else:
            print("No hay alumnos matriculados en cursos")
                
        
    except Exception as e:
        print(f"No se han podido mostrar los datos: {e}")
    
def mostrarRelacionesProfesores():
    print("--- Mostrar Asignaciones Profesor ---")

    """
    Se realiza una consulta multitabla entre profesores y cursos y mostrar los datos de la uniones
    """
    
    try:
        relaciones = (Profesor
                             .select(Profesor, Curso)
                             .join(ProfesorCurso)
                             .join(Curso)
                             .distinct())

        if (relaciones):
            # Iterar sobre los resultados e imprimir la información de cada profesor y el nombre del curso
            for relacion in relaciones:
                print("Profesor:")
                print("ID:", relacion.Id)
                print("DNI:", relacion.Dni)
                print("Nombre:", relacion.Nombre)
                print("Dirección:", relacion.Direccion)
                print("Teléfono:", relacion.Telefono)
                print("Curso:", relacion.Nombre)
                print()
        else:
            print("No hay profesores asignados a cursos")
        
        
    except Exception as e:
        print(f"No se han podido mostrar los datos: {e}")

def menuVinculaciones():
    

    """
    Menu vinculaciones para elegir una de las gestion mediante la insercion de un numero
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
            impartirCurso()
        elif(opcion=="2"):
            dejarImpartirCurso()
        elif(opcion=="3"):
            matricularAlumno()
        elif(opcion=="4"):
            desmatricularAlumno()
        elif(opcion=="5"):
            mostrarRelacionesAlumnos()
        elif(opcion=="6"):
            mostrarRelacionesProfesores()
        elif(opcion=="0"):
            finMenuVinculaciones = True
            print("Regresando a Menu Principal. Fin Menu Vinculaciones")
        else:
            print("Opcion no valida")