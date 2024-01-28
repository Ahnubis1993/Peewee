from Utilidades import confirmacion
from peewee import IntegrityError
from ModeloAlumno import Alumno
import re

def insertarAlumno():
    
    """
    Da de alta un alumno, si alguno de los atributos a asignar falla 5 veces, no se crea el alumno 
    y se pide si quieres dar de alta otro

    """
    
    fin = False
    while(not fin):
        print("\n--- Alta Alumno ---")
        
        intentos = 5
        correcto = False
        
        while(not correcto and intentos>0):
            expediente = input("Introduce el Numero de Expediente: ").strip()
            if(expediente.isdigit()): 
                correcto = True   
                print("Expediente valido")
            else:
                print("El expediente debe ser un numero")
            intentos -= 1 
        
        if (correcto):
            correcto = False
            intentos = 5
            
            while(not correcto and intentos>0):
                nombre = input("Introduce el nombre: ").strip()
                if(nombre != ""): 
                    correcto = True   
                    print("Nombre valido")
                else:
                    print("El nombre no puede estar vacio")
                intentos -= 1 

        if (correcto):
            correcto = False
            intentos = 5
            
            while(not correcto and intentos > 0):
                apellidos = input("Introduce los apellidos: ").strip()
                if(apellidos != ""): 
                    correcto = True   
                    print("Apellidos validos")
                else:
                    print("Los apellidos no pueden estar vacios")
                intentos -= 1 

        if (correcto):
            correcto = False
            intentos = 5
            
            while(not correcto and intentos>0):
                telefono = input("Introduce el telefono: ").strip()
                if(telefono.isdigit() and len(telefono)==9): 
                    correcto = True   
                    print("Telefono valido")
                else:
                    print("Telefono no valido. Deben ser 9 digitos sin espacios.")
                intentos -= 1 

        if (correcto):
            correcto = False
            intentos = 5
            
            while(not correcto and intentos>0):
                direccion = input("Introduce la direccion: ").strip()
                if(direccion != ""): 
                    correcto = True   
                    print("Direccion valida")
                else:
                    print("La direccion no puede estar vacia")
                intentos -= 1    

        if (correcto):
            correcto = False
            intentos = 5
            
            while(not correcto and intentos>0):
                fechaNac = input("Introduce la fecha de nacimiento (yyyy-mm-dd): ").strip()
                
                if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fechaNac):
                    correcto = True   
                    print("Fecha valida")
                else:
                    print("El formato de la fecha no es correcto. Debe ser yyyy-mm-dd")
                intentos -= 1   
                        
        if (correcto):
            try:
                Alumno.create(Num_Expediente = expediente, Nombre = nombre, Apellidos = apellidos, Telefono = telefono, Direccion = direccion, Fecha_Nacimiento = fechaNac)
                print("Alta realizada correctamente.")
                
            except IntegrityError as e:
                # Captura error de integridad de la base de datos
                if ("Duplicate entry" in str(e)):
                    if ("alumno_Nombre_Apellidos" in str(e)):
                        print("Ya existe un alumno con el mismo nombre y apellidos.")
                    else:
                        print("Ya existe un alumno con el mismo numero de expediente.")
                elif "Incorrect date value" in str(e):
                    print("La fecha de nacimiento no es correcta. Debe ser yyyy-mm-dd")
                else:
                    print("Error al introducir el alumno en la base de datos")
            except:
                print("Alumno no dado de alta, fallo al introducir el alumno en la base de datos")
                
        else:
            print("Has introducido el dato mal 5 veces. Alta cancelada.")
            
        if(not confirmacion("Deseas introducir otro alumno? (S/N): ")):
            fin = True
            print("Fin de alta de alumno")

def eliminarAlumno():
    """
    Elimina un alumno mediante el id que es buscado por el metodo busquedaAlumno
    Se obtiene el expediente del mismo y se elimina de las correspondientes tablas en la que se encuentre

    """

    alumnos = Alumno.select()

    if(alumnos):

        print("\n--- Baja Alumno ---")
        expediente = busquedaAlumno(True)
        if(expediente != -1):
            if (confirmacion("Estas seguro de que deseas eliminar el alumno con numero de expediente '"+str(expediente)+"'? (S/N)")):
                try:
                    Alumno.delete().where(Alumno.Num_Expediente == expediente).execute()
                    print("Alumno eliminado correctamente\n")
                except:
                    print("Error al eliminar el alumno de la base de datos")
            else:
                print("Alumno con expediente '"+str(expediente)+"' no ha sido dado de baja")
        else:
            print("No hay resultados de busqueda. Fin de baja de alumno")

    else:
        print("No hay alumnos en la BBDD")
    
def modificarAlumno():
    
    """
    Modifica un alumno que es buscado, mediante el expediente del alumno, 
    seleccionamos el atributo que se desee modificar siempre y cuando se acepte la confirmacion

    """
    print("\n--- Modificacion Alumno ---")

    alumnos = Alumno.select()

    if (alumnos):

        numExpediente = busquedaAlumno(True)
        finModificacion = False

        if(numExpediente != -1):
            while(not finModificacion):
                opcion = menuAtributos()
                if(opcion == "1"):
                    nuevoNumExpediente = input("Introduce el nuevo Numero de Expediente: ").strip()
                    if (nuevoNumExpediente.isdigit()):
                        try:
                            if(confirmacion("Estas seguro de que deseas modificar el numero de expediente? (S/N): ")):
                                Alumno.update(Num_Expediente=nuevoNumExpediente).where(Alumno.Num_Expediente == numExpediente).execute()
                                print("El numero de expediente ha sido modificado correctamente")
                            else:
                                print("Has cancelado la modificacion")
                        except Exception as e:
                            if "Duplicate entry" in str(e):
                                print("Ya existe un alumno con el mismo numero de expediente.")
                    else:
                        print("El numero de expediente debe ser un numero")
                elif(opcion == "2"):
                    nuevoNombre = input("Introduce el nuevo nombre: ").strip()
                    if(nuevoNombre!= ""):
                        try:
                            if(confirmacion("Estas seguro de que deseas modificar el nombre? (S/N): ")):
                                Alumno.update(Nombre=nuevoNombre).where(Alumno.Num_Expediente == numExpediente).execute()
                                print("El nombre ha sido modificado correctamente")
                            else:
                                print("Has cancelado la modificacion")
                        except Exception as e:
                            if "Duplicate entry" in str(e):
                                print("Ya existe un alumno con el mismo nombre y apellidos.")
                    else:
                        print("El nombre no puede estar vacio")
                elif(opcion == "3"):
                    nuevosApellidos = input("Introduce los nuevos apellidos: ").strip()
                    if(nuevosApellidos!= ""):
                        try:
                            if(confirmacion("Estas seguro de que deseas modificar los apellidos? (S/N): ")):
                                Alumno.update(Apellidos=nuevosApellidos).where(Alumno.Num_Expediente == numExpediente).execute()
                                print("Los apellidos han sido modificados correctamente")
                            else:
                                print("Has cancelado la modificacion")
                        except Exception as e:
                            if "Duplicate entry" in str(e):
                                print("Ya existe un alumno con el mismo nombre y apellidos.")
                    else:
                        print("Los apellidos no pueden estar vacios")
                elif(opcion == "4"):
                    nuevoTelefono = input("Introduce el nuevo telefono: ").strip()
                    if(nuevoTelefono.isdigit() and len(nuevoTelefono)==9):
                        try:
                            if(confirmacion("Estas seguro de que deseas modificar el telefono? (S/N): ")):
                                Alumno.update(Telefono = nuevoTelefono).where(Alumno.Num_Expediente == numExpediente).execute()
                                print("El telefono ha sido modificado correctamente")
                            else:
                                print("Has cancelado la modificacion")
                        except:
                            print("El telefono no se ha podido modificar correctamente")
                    else:
                        print("El telefono debe tener 9 digitos")
                elif(opcion == "5"):
                    nuevaDireccion = input("Introduce la nueva direccion: ").strip()
                    if(nuevaDireccion!= ""):
                        try:
                            if(confirmacion("Estas seguro de que deseas modificar la direccion? (S/N): ")):
                                Alumno.update(Direccion = nuevaDireccion).where(Alumno.Num_Expediente == numExpediente).execute()
                                print("La direccion ha sido modificada correctamente")
                            else:
                                print("Has cancelado la modificacion")
                        except:
                            print("La direccion no se ha podido modificar correctamente")
                    else:
                        print("La direccion no puede estar vacia")
                elif(opcion == "6"):
                    nuevaFechaNac = input("Introduce la nueva fecha de nacimiento (yyyy-mm-dd): ").strip()
                    if("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", nuevaFechaNac):
                        try:
                            if(confirmacion("Estas seguro de que deseas modificar la fecha de nacimiento? (S/N): ")):
                                Alumno.update(Fecha_Nacimiento = nuevaFechaNac).where(Alumno.Num_Expediente == numExpediente).execute()
                                print("La fecha de nacimiento ha sido modificada correctamente")
                            else:
                                print("Has cancelado la modificacion")
                        except Exception as e:
                            if "Incorrect date value" in str(e):
                                print("La fecha de nacimiento no es correcta. Debe ser yyyy-mm-dd")
                    else:
                        print("La fecha de nacimiento no es correcta. Debe ser yyyy-mm-dd")

                elif(opcion=="0"):
                    finModificacion = True
                    print("Fin de modificacion de alumno")
                else:
                    print("Opcion no valida")

                if(not finModificacion and not confirmacion("Deseas modificar otro atributo de este alumno? (S/N): ")):
                    finModificacion = True
        else:
            print("No hay resultados de busqueda. Fin de modificacion de alumno")
    else:
        print("No hay alumnos en la BBDD")

def busquedaAlumno(alumnoUnico = False):
    
    """
    Busca un alumno mediante cualquier atributo del mismo, si es localizado se devuelve el expediente 
    pera poder gestionarlo en otros metodos

    """
    
    print("\n--- Busqueda Alumno ---")

    alumnos = Alumno.select()

    if (alumnos):

        numExpediente = -1
        finBusqueda = False

        while(not finBusqueda):
            query = None
            cantidadResultados = 0
            opcion = menuAtributos()
            if (opcion == "1"):
                expediente = input("Introduce el Numero de Expediente a buscar: ").strip()
                if (expediente.isdigit()):
                    try:
                        query = Alumno.select().where(Alumno.Num_Expediente == expediente)
                    except:
                        print("Consulta por Numero de Expediente no valida")
                else:
                    print("Debes buscar por un numero")

            elif (opcion == "2"):
                nombre = input("Introduce el Nombre a buscar: ").strip()
                if(nombre!= ""):
                    try:
                        query = Alumno.select().where(Alumno.Nombre == nombre)
                    except:
                        print("Consulta por Nombre no valida")
                else:
                    print("No puedes buscar por un nombre vacio")

            elif (opcion == "3"):
                apellidos = input("Introduce los Apellidos a buscar: ").strip()
                if(apellidos!= ""):
                    try:
                        query = Alumno.select().where(Alumno.Apellidos == apellidos)
                    except:
                        print("Consulta por Apellidos no valida")
                else:
                    print("No puedes buscar por apellidos vacios")

            elif (opcion == "4"):
                telefono = input("Introduce el Telefono a buscar: ").strip()
                if(telefono.isdigit() and len(telefono)==9):
                    try:
                        query = Alumno.select().where(Alumno.Telefono == telefono)
                    except:
                        print("Consulta por Telefono no valida")
                else:
                    print("Telefono no valido. Deben ser 9 digitos sin espacios.")

            elif (opcion == "5"):
                direccion = input("Introduce la direccion a buscar: ").strip()
                if(direccion!= ""):
                    try:
                        query = Alumno.select().where(Alumno.Direccion == direccion)
                    except:
                        print("Consulta por Direccion no valida")
                else:
                    print("No puedes buscar por una direccion vacia")

            elif (opcion == "6"):
                fechaNac = input("Introduce la fecha de nacimiento a buscar (yyyy-mm-dd): ").strip()

                if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fechaNac):
                    try:
                        query = Alumno.select().where(Alumno.Fecha_Nacimiento == fechaNac)
                    except:
                        print("Consulta por Fecha de Nacimiento no valida")
                else:
                    print("El formato de la fecha no es correcto. Debe ser yyyy-mm-dd")

            elif(opcion=="0"):
                finBusqueda = True
                print("Fin de busqueda de Alumno")
            else:
                print("Opcion no valida")

            if(not finBusqueda):
                if (query is not None):
                    cantidadResultados = query.count()

                print("--- Resultado de la Busqueda ---")
                if (cantidadResultados > 0):
                    for alumno in query:
                        print("Numero de expediente:"+str(alumno.Num_Expediente)+"\n"
                            "Nombre:"+alumno.Nombre+"\n"
                            "Apellidos:"+alumno.Apellidos+"\n"
                            "Telefono:"+alumno.Telefono+"\n"
                            "Direccion:"+alumno.Direccion+"\n"
                            "Fecha de Nacimiento:"+str(alumno.Fecha_Nacimiento)+"\n"
                            "--------------------------------\n")

                if(cantidadResultados > 1 and alumnoUnico):
                    finAlumnoUnico = False
                    while(not finAlumnoUnico):
                        expediente = input("Introduce el numero de expediente del alumno a elegir: ")
                        if(expediente.isdigit()):
                            numExpedienteEncontrado = False
                            for alumno in query:
                                if (alumno.Num_Expediente == int(expediente)):
                                    numExpedienteEncontrado = True
                                    finAlumnoUnico = True
                                    finBusqueda = True
                                    numExpediente = expediente

                            if (not numExpedienteEncontrado):
                                print("No existe ningun alumno con ese numero de expediente")
                        else:
                            print("Tienes que insertar un numero")
                elif(cantidadResultados==1):
                    finBusqueda = True
                    numExpediente = query[0].Num_Expediente
                elif(cantidadResultados==0):
                    if(not confirmacion("No se han encontrado resultados. Deseas buscar de nuevo? (S/N): ")):
                        finBusqueda = True
        return numExpediente
    else:
        print("No hay alumnos en la BDD")

def mostrarTodos():
    
    """
    Muestra todos los alumnos que haya en la tabla Alumnos
    
    """
    
    print("\n--- Mostrando todos los alumnos ---")

    alumnos = Alumno.select()

    if (alumnos):

        try:
            query = Alumno.select()

            if (len(query)==0):
                print("No hay alumnos registrados")

            for alumno in query:
                    print("Numero de expediente:"+str(alumno.Num_Expediente)+"\n"
                          "Nombre:"+alumno.Nombre+"\n"
                          "Apellidos:"+alumno.Apellidos+"\n"
                          "Telefono:"+alumno.Telefono+"\n"
                          "Direccion:"+alumno.Direccion+"\n"
                          "Fecha de Nacimiento:"+str(alumno.Fecha_Nacimiento)+"\n"
                          "--------------------------------")
        except:
            print("No se han podido mostrar todos los alumnos")

    else:
        print("No hay alumnos en la BBDD")
    
def menuAtributos(): 
    
    """
    Menu de atributos del alumno entre los que se pueden elegir

    """
    
    fin = False
    while(not fin):
        print("Elige un atributo de los siguientes: ")
        print("--- Atributos ---")
        print("1 - Numero de expediente")
        print("2 - Nombre")
        print("3 - Apellidos")
        print("4 - Telefono")
        print("5 - Direccion")
        print("6 - Fecha de Nacimiento")
        print("0 - Salir")
        opcion = input("Introduce una opcion: ")
        if(opcion.isdigit() and 0 <= int(opcion) <= 6):
            fin = True          
        else:
            print("Opcion no valida")
    return opcion

def menuAlumnos():
    
    """
    Menu de alumnos donde se pueden elegir las diferentes operaciones de gestion relacionados con el mismo
    Se pedira una opcion para entrar en alguno de los submenus, si insertas 0, sale al menuPrincipal

    """
    
    finMenuAlumno = False
    
    while(finMenuAlumno is False):
        
        print("\n--- Menu Alumnos ---")
        print("1 - Alta")
        print("2 - Baja")
        print("3 - Modificar")
        print("4 - Busqueda")
        print("5 - Mostrar Todos")
        print("0 - Salir")
        opcion = input("Introduce una Opcion: ").strip()
        
        if(opcion=="1"):
            insertarAlumno()
        elif(opcion=="2"):
            eliminarAlumno()
        elif(opcion=="3"):
            modificarAlumno()
        elif(opcion=="4"):
            busquedaAlumno()
        elif(opcion=="5"):
            mostrarTodos()
        elif(opcion=="0"):
            finMenuAlumno = True
            print("Regresando a Menu Principal")
        else:
            print("Opcion incorrecta")