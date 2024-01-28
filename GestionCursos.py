from pymysql import IntegrityError
from Utilidades import confirmacion
from ModeloCurso import Curso

def insertarCurso():
    
    """
    Descripción corta de la función.

    Da de alta un curso, si alguno de los atributos a asignar falla 5 veces, no se crea el curso 
    y se pide si quieres dar de alta otro

    """
    fin = False
    while(not fin):
        print("--- Alta Curso ---")
        
        correcto = False
        intentos = 5
        
        while(not correcto and intentos>0):
            nombreCurso = input("Introduce nombre del curso: ").strip()
            if(nombreCurso != ""):
                correcto = True
                print("Nombre del curso valido")
            else:
                print("El nombre no puede estar vacio")
            intentos -= 1
        
        if(correcto):
            
            correcto = False
            intentos = 5
            
            while(not correcto and intentos>0):
                descripcionCurso = input("Introduce la descripcion del curso: ").strip()
                if(descripcionCurso != ""):
                    correcto = True
                    print("Descripcion del curso valida")
                else:
                    print("La descripcion del curso no puede estar vacia")
                intentos -= 1
        
        if(correcto):
            try:
                Curso.create(Nombre=nombreCurso, Descripcion=descripcionCurso)
                print("Alta del Curso realizada correctamente")
                
            except IntegrityError as e:
                if ("Duplicate entry" in str(e)):
                    print("Ya existe un curso con ese Nombre")
                else:
                    print("Error al introducir el Curso en la base de datos")
            except:
                print("Curso no dado de alta, fallo al introducir el Curso en la base de datos")
        else:
            print("Has introducido el dato mal 5 veces. Alta cancelada.")
            
        if(not confirmacion("Deseas introducir otro Curso? (S/N): ")):
            fin = True
            print("Fin alta Curso")
    

def eliminarCursor(conexionBBDD):
    
    """
    Elimina un curso mediante el id que es buscado por el metodo busquedaCurso
    Se obtiene el id del mismo y se elimina de las correspondientes tablas en la que se encuentre

    :param parametro1: conexion a bbdd
    """
    
    print("--- Baja Curso ---")
    codigoCurso = busquedaCurso(conexionBBDD)
    if(codigoCurso != -1):
        if(confirmacion("Estas seguro de que deseas eliminar el curso con codigo '"+str(codigoCurso)+"'? (S/N): ")):
            try:
                cursor = conexionBBDD.cursor()
                cursor.execute("DELETE FROM Cursos WHERE Codigo=%s",codigoCurso)
                conexionBBDD.commit()
                print("Curso con codigo '"+str(codigoCurso)+"' eliminado correctamente")
            except:
                print("Error al eliminar el curso de la base de datos")
            finally: 
                if (cursor is not None):
                    cursor.close()
        else:
            print("Curso con codigo '"+str(codigoCurso)+"' no ha sido dado de baja")
    else:
        print("No hay resultados de busqueda. Fin baja Curso")
    
def modificarCurso(conexionBBDD):
    
    """
    Modifica un curso que es buscado, mediante el id
    del curso, seleccionamos el atributo que se desee modificar siempre y cuando se acepte la confirmacion

    :param parametro1: conexion a bbdd
    """
    
    print("--- Modificacion Curso ---")
    
    codigoCurso = busquedaCurso(conexionBBDD)  
    finModificacionCurso = False
    modificado = False
    
    if(codigoCurso != -1):
        while(not finModificacionCurso):  
            print("Elige un atributo de los siguientes: ")
            print("--- Atributos ---")
            print("1 - Nombre")
            print("2 - Descripcion")
            print("0 - Salir")
            opcion = input("Introduce una opcion: ").strip()
            
            if(opcion=="1"):
                nuevoNombreCurso = input("Introduce nuevo nombre a modificar: ").strip()
                if(nuevoNombreCurso != ""):
                    try:
                        if(confirmacion("Estas seguro de que deseas modificar el nobre del curso, (S/N): ")):
                            cursor = conexionBBDD.cursor()
                            cursor.execute("UPDATE Cursos SET Nombre=%s WHERE Codigo=%s", (nuevoNombreCurso, codigoCurso))
                            conexionBBDD.commit()
                            print("El nombre del curso se ha modificado correctamente")
                            modificado =True
                        else:
                            print("Has cancelado la modificacion")
                    except:
                        print("Consulta por nombre no valida")
                    finally: 
                        if (cursor is not None):
                            cursor.close()
                else:
                    print("El nombre del curso no puede estar vacio")
            elif(opcion=="2"):
                descripcionCurso = input("Introduce nueva descripcion del curso a modificar: ").strip()
                if(descripcionCurso != ""):
                    try:
                        if(confirmacion("Estas seguro de que deseas modificar la descripcion del curso, (S/N): ")):
                            cursor = conexionBBDD.cursor()
                            cursor.execute("UPDATE Cursos SET Descripcion=%s WHERE Codigo=%s", (descripcionCurso, codigoCurso))
                            conexionBBDD.commit()
                            print("La descripcion del curso se ha modificado correctamente")
                            modificado =True
                        else:
                            print("Has cancelado la modificacion")    
                    except:
                        print("Consulta por descripcion no valida")
                    finally: 
                        if (cursor is not None):
                            cursor.close()
                else:
                    print("La descripcion el curso no puede estar vacia")
                
            elif(opcion=="0"):
                finModificacionCurso = True
                print("Fin Modificacioi Curso")
            else:
                print("Opcion no valida")
                
            if(modificado):
                if(not confirmacion("Deseas modificar algo mas de este curso? (S/N): ")):
                    finModificacionCurso = True
            else:
                if(not confirmacion("No has modificado ningun atributo de curso. Deseas modificar alguno? (S/N): ")):
                    finModificacionCurso = True
                    
    else:
        print("No hay resultados de busqueda. Fin modificacion Curso")   
        
def busquedaCurso(conexionBBDD):
    
    """
    Busca un curso mediante cualquier atributo del mismo, si es localizado se devuelve el id 
    pera poder gestionarlo en otros metodos

    :param parametro1: conexion a bbdd
    """
    
    codigoCurso = -1
    finBusquedaCurso = False
    filasTablaCurso = []
    
    while(not finBusquedaCurso):
        
        print("Elige un atributo de los siguientes: ")
        print("--- Atributos ---")
        print("1 - Nombre")
        print("2 - Descripcion")
        print("0 - Salir")
        opcion = input("Introduce una opcion: ").strip()
        
        if(opcion=="1"):
            nombreCurso = input("Introduce nombre del curso a buscar: ").strip()
            if(nombreCurso != ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Cursos WHERE Nombre=%s", (nombreCurso))
                    filasTablaCurso = cursor.fetchall()
                except:
                    print("Consulta por nombre no valida")
                finally: 
                    if (cursor is not None):
                        cursor.close()

            else:
                print("El nombre del curso no puede estar vacio")
        elif(opcion=="2"):
            descripcionCurso = input("Introduce descripcion del curso a buscar: ").strip()
            if(descripcionCurso != ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Cursos WHERE Descripcion=%s", (descripcionCurso))
                    filasTablaCurso = cursor.fetchall()
                except:
                    print("Consulta por descripcion no valida")
                finally: 
                    if (cursor is not None):
                        cursor.close()
            else:
                print("La descripcion el curso no puede estar vacia")
            
        elif(opcion=="0"):
            finBusquedaCurso = True
            print("Fin busqueda Curso")
        else:
            print("Opcion no valida")
            
        if(not finBusquedaCurso and filasTablaCurso):
            print("--- Resultado de la busqueda ---")
            for f in filasTablaCurso:
                print("Codigo:"+str(f[0])+"\n"
                    "Nombre:"+f[1]+"\n"
                    "Descripcion:"+f[2]+"\n"
                "--------------------------------\n")
            
            if(len(filasTablaCurso)>1):
                finBusquedaIdCurso = False
                while(not finBusquedaIdCurso):
                    codigoCurso = input("Introduce el id del curso a elegir")
                    if(codigoCurso.isdigit()):
                        codigoCursoEncontrado = [fila for fila in filasTablaCurso if(f[0]==int(codigoCurso))]
                        if(codigoCursoEncontrado):
                            codigoCurso = codigoCursoEncontrado[0]
                            finBusquedaIdCurso = True
                    else:
                        print("Tienes que insertar un numero")
            elif(len(filasTablaCurso)==1):
                codigoCurso = filasTablaCurso[0][0]
                finBusquedaCurso = True
        else:
            if(not confirmacion("No se han encontrado resultados. Deseas buscar de nuevo? (S/N): ")):
                finBusquedaCurso = True 
        
    return codigoCurso

def mostrarTodosCursos(conexionBBDD):
    
    """
    Muestra todos los cursos que haya en la tabla Cursos

    :param parametro1: conexion a bbdd
    """
    
    print("--- Mostrar Todos los Cursos ---")
    
    try:
        cursor=conexionBBDD.cursor()
        cursor.execute("SELECT * FROM Cursos")
        filas = cursor.fetchall()
        
        if(len(filas)==0):
            print("No hay cursos registrados")
        
        for f in filas:
            print("Codigo:"+str(f[0])+"\n"
                    "Nombre:"+f[1]+"\n"
                    "Descripcion:"+f[2]+"\n"
            "--------------------------------\n")
            
    except:
        print("No se han podido mostrar todos los cursos")
    finally: 
        if (cursor is not None):
            cursor.close()
    
def menuCursos(conexionBBDD):
    
    """
    Menu de cursos donde se pueden elegir las diferentes operaciones de gestion relacionados con el mismo
    Se pedira una opcion para entrar en alguno de los submenus, si insertas 0, sale al menuPrincipal

    :param parametro1: conexion a bbdd
    """
    
    finMenuCurso = False
    
    while(not finMenuCurso):
        
        print("--- Menu Cursos ---")
        print("1 - Alta")
        print("2 - Baja")
        print("3 - Modificar")
        print("4 - Busqueda")
        print("5 - Mostrar Todos")
        print("0 - Salir")
        opcion = input("Introduce una Opcion: ").strip()
        
        if(opcion=="1"):
            insertarCurso(conexionBBDD)
        elif(opcion=="2"):
            eliminarCursor(conexionBBDD)
        elif(opcion=="3"):
            modificarCurso(conexionBBDD)
        elif(opcion=="4"):
            busquedaCurso(conexionBBDD)
        elif(opcion=="5"):
            mostrarTodosCursos(conexionBBDD)
        elif(opcion=="0"):
            finMenuCurso = True
            print("Regresando a Menu Principal")
        else:
            print("Opcion incorrecta")