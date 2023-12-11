from Utilidades import confirmacion
from pymysql import IntegrityError


def insertarProfesor(conexionBBDD):
    
    """
    Descripción corta de la función.

    Da de alta un profesor, si alguno de los atributos a asignar falla 5 veces, no se crea el profesor 
    y se pide si quieres dar de alta otro

    :param parametro1: conexion a bbdd
    """
    
    print("--- Alta Profesor ---")
    
    intentos = 5
    correcto = False
    
    while(not correcto):
    
        while(not correcto and intentos>0):
            dniProfesor = input("Introduce el dni del profesor: ").strip()
            if(len(dniProfesor)==9 and dniProfesor[8:].isdigit and dniProfesor[8:].isalpha): 
                correcto = True   
                print("el dni introducido es valido")
            else:
                print("El dni debe esta formado por 8 digitos y 1 letra")
            intentos -= 1 
        
        if(correcto):
            correcto = False
            intentos = 5
            
            while(not correcto and intentos>0):
                nombreProfesor = input("Introduce el nombre del profesor: ").strip()
                if(nombreProfesor != ""): 
                    correcto = True   
                    print("El nombre introducido es valido")
                else:
                    print("El nombre no puede estar vacio")
                intentos -= 1 

        if(correcto):
            correcto = False
            intentos = 5
            
            while(not correcto and intentos>0):
                direccionProfesor = input("Introduce la direccion del profesor: ").strip()
                if(direccionProfesor != ""): 
                    correcto = True   
                    print("La direccion introducida es valida")
                else:
                    print("La direccion no puede estar vacia")
                intentos -= 1    

        if(correcto):
            correcto = False
            intentos = 5
            
            while(not correcto and intentos>0):
                telefonoProfesor = input("Introduce el telefono del profesor: ").strip()
                if(telefonoProfesor.isdigit() and len(telefonoProfesor)==9): 
                    correcto = True   
                    print("El telefono introducido es valido")
                else:
                    print("El telefono debe tener una longitud de 9 digitos")
                intentos -= 1 
            
            
        if(correcto):
            # se pone a false porque viene true, para poder ingresar otro profesor
            correcto = False   
            try:
                cursor = conexionBBDD.cursor()
                cursor.execute("INSERT INTO Profesores (dni, nombre, direccion, telefono) VALUES (%s, %s, %s, %s)",
                            (dniProfesor.upper(), nombreProfesor, direccionProfesor, telefonoProfesor))
                conexionBBDD.commit()
                
                if(not confirmacion("El alta del profesor se ha realizado correctamente. Deseas introducir otro profesor? (S/N): ")):
                    correcto = True
                    print("Fin alta Profesor")
                    
            except IntegrityError as e:
                if "Dni_UNIQUE" in str(e):
                    print("Ya existe un profesor con mismo DNI.")
                else:
                    print("Error al introducir el curso en la base de datos")
            except Exception:
                print("Profesor no dado de alta, fallo al introducir el profesor en la base de datos")
            finally: 
                if (cursor is not None):
                    cursor.close()

        else:
            correcto = False
            if(not confirmacion("El alta del profesor no se ha realizado correctamente. Deseas introducir un profesor? (S/N): ")):
                correcto = True
                print("Fin alta Profesor")
            
def eliminarProfesor(conexionBBDD):
    
    """
    Descripción corta de la función.

    Elimina un profesor mediante el id que es buscado por el metodo busquedaProfesor
    Se obtiene el id del mismo y se elemina de las correspondientes tablas en la que se encuentre

    :param parametro1: conexion a bbdd
    """
    
    print("--- Baja Profesor ---")
    idProfesor = busquedaProfesor(conexionBBDD)
    if(idProfesor != -1):
        try:
            cursor = conexionBBDD.cursor()
            if(confirmacion("Estas seguro de que deseas eliminar el profesor? (S/N): ")):
                cursor.execute("DELETE FROM Profesores WHERE Id=%s",(idProfesor))
                conexionBBDD.commit()
                print("Profesor dado de baja correctamente\n")
            else:
                print("Has cancelado la baja del profesor")

        except:
            #TODO
            print("Consulta de borrado Profesor no valida")
        finally:
            if (cursor is not None):
                cursor.close()
            
    else:
        print("No hay resultados de busqueda. Fin baja profesor")
    
def modificarProfesor(conexionBBDD):
    
    """
    Descripción corta de la función.

    Modifica un profesor mediante que es buscado por id en metodo busqueda, mediante el id
    del profesor, seleccionamos el atributo que se desee modificar siempre y cuando se acepte la confirmacion

    :param parametro1: conexion a bbdd
    """
    
    print("--- Modificacion Profesor ---")
    
    idProfesor = busquedaProfesor(conexionBBDD) 
    finModificacionProfesor = False
    modificado = False
    
    if(idProfesor != -1):
        while(not finModificacionProfesor): 
            opcion = menuAtributos()
            
            if(opcion=="1"):
                nuevoDniProfesor = input("Introduce nuevo dni del profesor: ").strip()
                if(len(nuevoDniProfesor)==9 and nuevoDniProfesor[8:].isdigit and nuevoDniProfesor[8:].isalpha):
                    try:
                        
                        if(confirmacion("Estas seguro de que deseas modificar el dni del profesor? (S/N): ")):
                            cursor = conexionBBDD.cursor()
                            cursor.execute("UPDATE Profesores SET Dni=%s WHERE Id=%s", (nuevoDniProfesor, idProfesor))
                            conexionBBDD.commit()
                            print("El dni del profesor ha sido modificado correctamente")
                            modificado = True
                        else:
                            print("Has cancelado la modificacion")
                    except IntegrityError as e:
                        if "Dni_UNIQUE" in str(e):
                            print("Ya existe un profesor con mismo DNI.")
                    except Exception:
                        print("Consulta por Dni no valida")
                    finally:
                        if (cursor is not None):
                            cursor.close()
                else:
                    print("El dni debe esta formado por 8 digitos y 1 letra")
            elif(opcion=="2"):
                nuevoNombreProfesor = input("Introduce nuevo nombre del profesor: ").strip()
                if(nuevoNombreProfesor != ""):
                    try:
                        if(confirmacion("Estas seguro de que deseas modificar el nombre del profesor? (S/N): ")):
                            cursor = conexionBBDD.cursor()
                            cursor.execute("UPDATE Profesores SET Nombre=%s WHERE Id=%s", (nuevoNombreProfesor, idProfesor))
                            conexionBBDD.commit()
                            print("El nombre del profesor ha sido modificado correctamente")
                            modificado = True
                        else:
                            print("Has cancelado la modificacion")
                    except:
                        print("Consulta por Nombre no valida")
                    finally:
                        if (cursor is not None):
                            cursor.close()
                else:
                    print("El nombre no puede estar vacio")
                
            elif(opcion=="3"):
                nuevaDireccionProfesor = input("Introduce nueva direccion del profesor: ").strip()
                if(nuevaDireccionProfesor != ""):
                    try:
                        if(confirmacion("Estas seguro de que deseas modificar la direccion del profesor? (S/N): ")):
                            cursor = conexionBBDD.cursor()
                            cursor.execute("UPDATE Profesores SET Direccion=%s WHERE Id=%s", (nuevaDireccionProfesor, idProfesor))
                            conexionBBDD.commit()
                            print("La direccion del profesor ha sido modificada correctamente")
                            modificado = True
                        else:
                            print("Has cancelado la modificacion")
                    except:
                        print("Consulta por Direccion no valida")
                    finally:
                        if (cursor is not None):
                            cursor.close()
                else:
                    print("La direccion no puede estar vacia")
            
            elif(opcion=="4"):
                nuevoTelefonoProfesor = input("Introduce nuevo telefono del profesor: ").strip()
                if(nuevoTelefonoProfesor.isdigit() and len(nuevoTelefonoProfesor)==9):
                    try: 
                        if(confirmacion("Estas seguro de que deseas modificar el telefono del profesor? (S/N): ")):
                            cursor = conexionBBDD.cursor()
                            cursor.execute("UPDATE Profesores SET Telefono=%s WHERE Id=%s", (nuevoTelefonoProfesor, idProfesor))
                            conexionBBDD.commit()
                            print("El telefono del profesor ha sido modificado correctamente")  
                            modificado = True
                        else:
                            print("Has cancelado la modificacion")                                        
                    except:
                        print("Consulta por Telefono no valida")
                    finally:
                        if (cursor is not None):
                            cursor.close()
                else:
                    print("El telefono debe tener una longitud de 9 digitos")
                
            elif(opcion=="0"):
                finModificacionProfesor = True
                print("Fin busqueda Profesor")
            else:
                print("Opcion no valida")
                
            if(modificado):
                if(not confirmacion("Deseas modificar algo mas de este profesor? (S/N): ")):
                    finModificacionProfesor = True
            else:
                if(not confirmacion("No has modificado ningun atributo de profesor. Deseas modificar alguno? (S/N): ")):
                    finModificacionProfesor = True
                
    else:
        print("No hay resultados de busqueda. Fin modificar profesor")
        
def busquedaProfesor(conexionBBDD):
    
    """
    Descripción corta de la función.

    Busca un profesor mediante cualquier atributo del mismo, si es localizado se devuelve el id 
    pera poder gestionarlo en otros metodos

    :param parametro1: conexion a bbdd
    """
    
    print("--- Busqueda Profesor ---")
    
    idProfesor = -1
    finBusquedaProfesor = False
    filasTablaProfesor = []
    
    while(not finBusquedaProfesor):
        opcion = menuAtributos()
        
        if(opcion=="1"):
            dniProfesor = input("Introduce dni del profesor a buscar: ").strip()
            if(len(dniProfesor)==9 and dniProfesor[8:].isdigit and dniProfesor[8:].isalpha):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Dni=%s", (dniProfesor))
                    filasTablaProfesor = cursor.fetchall()
                except:
                    print("Consulta por Dni no valida")
                finally:
                    if (cursor is not None):
                        cursor.close()
            else:
                print("El dni debe esta formado por 8 digitos y 1 letra")
        elif(opcion=="2"):
            nombreProfesor = input("Introduce nombre del profesor a buscar: ").strip()
            if(nombreProfesor != ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Nombre=%s", (nombreProfesor))
                    filasTablaProfesor = cursor.fetchall()
                except:
                    print("Consulta por Nombre no valida")
                finally:
                    if (cursor is not None):
                        cursor.close()
            else:
                print("El nombre no puede estar vacio")
            
        elif(opcion=="3"):
            direccionProfesor = input("Introduce direccion del profesor a buscar").strip()
            if(direccionProfesor != ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Direccion=%s",(direccionProfesor))
                    filasTablaProfesor = cursor.fetchall()
                    cursor.close()
                except:
                    print("Consulta por Direccion no valida")
                finally:
                    if (cursor is not None):
                        cursor.close()
            else:
                print("La direccion no puede estar vacia")
        
        elif(opcion=="4"):
            telefonoProfesor = input("Introduce telefono del profesor a buscar: ").strip()
            if(telefonoProfesor.isdigit() and len(telefonoProfesor)==9):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Telefono=%s", (telefonoProfesor))
                    filasTablaProfesor = cursor.fetchall()
                except:
                    print("Consulta por Telefono no valida")
                finally:
                    if (cursor is not None):
                        cursor.close()
            else:
                print("El telefono debe tener una longitud de 9 digitos")
            
        elif(opcion=="0"):
            finBusquedaProfesor = True
            print("Fin busqueda Profesor")
        else:
            print("Opcion no valida")
            
        if(not finBusquedaProfesor and filasTablaProfesor):
            print("--- Resultado ---")
            
            for f in filasTablaProfesor:
                print("Id_Profesor:"+str(f[0])+"\n"
                      "Dni:"+f[1]+"\n"
                      "Nombre:"+f[2]+"\n"
                      "Direccion:"+f[3]+"\n"
                      "Telefono:"+str(f[4])+"\n"
                      "--------------------------------\n")
            
            if(len(filasTablaProfesor)>1):
                finIdProfesor = False
                while(not finIdProfesor):
                    idProfesorBuscar = input("Introduce el id del profesor a elegir")
                    if(idProfesorBuscar.isdigit()):
                        idProfesorEncontrado = [fila for fila in filasTablaProfesor if(fila[0]==int(idProfesorBuscar))]
                        if(idProfesorEncontrado):
                            idProfesor = idProfesorEncontrado[0]
                            finBusquedaProfesor = True
                    else:
                        print("Tienes que insertar un numero")
            elif(len(filasTablaProfesor)==1):
                idProfesor = filasTablaProfesor[0][0]
                finBusquedaProfesor = True
        else:
            if(not confirmacion("No se han encontrado resultados. Deseas buscar de nuevo? (S/N): ")):
                finBusquedaProfesor = True
    return idProfesor
    

def mostrarTodosProfesores(conexionBBDD):
    
    """
    Descripción corta de la función.

    Muestra todos los profesores que haya en la tabla Profesores

    :param parametro1: conexion a bbdd
    """
    
    print("--- Mostrar Todos los Profesores ---")
    
    try:
        cursor=conexionBBDD.cursor()
        cursor.execute("SELECT * FROM Profesores")
        filas = cursor.fetchall()
        
        if(len(filas)==0):
            print("No hay profesores registrados")
        
        for f in filas:
            print("Id_Profesor:"+str(f[0])+"\n"
                    "Dni:"+f[1]+"\n"
                    "Nombre:"+f[2]+"\n"
                    "Direccion:"+f[3]+"\n"
                    "Telefono:"+str(f[4])+"\n"
                    "--------------------------------\n")
            
    except:
        print("No se han podido mostrar todos los profesores")
    finally: 
        if (cursor is not None):
            cursor.close()
    
def menuAtributos(): 
    
    """
    Descripción corta de la función.

    Menu de profesores donde se pueden elegir las diferentes operaciones de gestion relacionados con el mismo
    Se pedir una opcion para entrar en alguno de los submenus, si insertas 0, sale al menuPrincipal

    :param parametro1: conexion a bbdd
    """
    
    print("Elige un atributo de los siguientes: ")
    print("--- Atributos ---")
    print("1 - Dni")
    print("2 - Nombre")
    print("3 - Direccion")
    print("4 - Telefono")
    print("0 - Salir")
    opcion = input("Introduce una opcion: ").strip()
    return opcion
    
def menuProfesores(conexionBBDD):
    
    finMenuProfesor = False
    
    while(not finMenuProfesor):
        
        print("--- Menu Profesores ---")
        print("1 - Alta")
        print("2 - Baja")
        print("3 - Modificar")
        print("4 - Busqueda")
        print("5 - Mostrar Todos")
        print("0 - Salir")
        opcion = input("Introduce una Opcion: ").strip()
        
        if(opcion=="1"):
            insertarProfesor(conexionBBDD)
        elif(opcion=="2"):
            eliminarProfesor(conexionBBDD)
        elif(opcion=="3"):
            modificarProfesor(conexionBBDD)
        elif(opcion=="4"):
            busquedaProfesor(conexionBBDD)
        elif(opcion=="5"):
            mostrarTodosProfesores(conexionBBDD)
        elif(opcion=="0"):
            finMenuProfesor = True
            print("Regresando a Menu Principal. Fin Menu Profesores")
        else:
            print("Opcion no valida")       