from Utilidades import confirmacion
from peewee import IntegrityError, DoesNotExist
from ModeloProfesor import Profesor


def insertarProfesor():

    """
    Da de alta un profesor, si alguno de los atributos a asignar falla 5 veces, no se crea el profesor 
    y se pide si quieres dar de alta otro
    """

    fin = False

    while (not fin):

        print("--- Alta Profesor ---")

        intentos = 5
        correcto = False

        while(not correcto and intentos>0):

            dniProfesor = input("Introduce el DNI del profesor: ").strip()
            if(len(dniProfesor)==9 and dniProfesor[8:].isdigit and dniProfesor[8:].isalpha):
                # Ponemos el ultimo caracter (La letra del DNI) en mayuscula
                dniProfesor = dniProfesor[:8] + dniProfesor[8:].upper()
                correcto = True
                print("El DNI introducido es valido")
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
                # isDigit comprueba que la variable (String como el modelo en Char) solo son numerica, no que sea un "integer"
                if(telefonoProfesor.isdigit() and len(telefonoProfesor)==9):
                    correcto = True
                    print("El telefono introducido es valido")
                else:
                    print("El telefono debe tener una longitud de 9 digitos")
                intentos -= 1


        if(correcto):

            try:
                Profesor.create(Dni=dniProfesor, Nombre=nombreProfesor, Direccion=direccionProfesor,Telefono=telefonoProfesor)
                print("Alta realizada correctamente")
            except IntegrityError as e:
                if "Duplicate entry" in str(e):
                    print("Ya existe un profesor con el mismo DNI.")
                else:
                    print("Error al introducir el profesor en la base de datos")

        else:
            print("Has introducido el dato mal 5 veces. Alta cancelada.")

        if(not confirmacion("Deseas introducir otro profesor? (S/N): ")):
            fin = True
            print("Fin de alta de Profesor")

def eliminarProfesor():

    """
    Elimina un profesor mediante el id que es buscado por el metodo busquedaProfesor
    Se obtiene el id del mismo y se elimina de las correspondientes tablas en la que se encuentre
    """

    print("--- Baja Profesor ---")
    idProfesor = busquedaProfesor(True)

    if(idProfesor != -1):

        if(confirmacion("Estas seguro de que deseas eliminar el profesor con id '"+str(idProfesor)+"'? (S/N): ")):
                Profesor.delete().where(Profesor.Id == idProfesor).execute()
                print("Profesor con id "+str(idProfesor)+" ha sido dado de baja")
        else:
            print("Profesor con id '"+str(idProfesor)+"' no ha sido dado de baja")

    else:
        print("No hay resultados de busqueda. Fin baja profesor")

def modificarProfesor():

    """
    Modifica un profesor que es buscado, mediante el id
    del profesor, seleccionamos el atributo que se desee modificar siempre y cuando se acepte la confirmacion
    """

    print("--- Modificacion Profesor ---")

    idProfesor = busquedaProfesor(True)
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
                            Profesor.update(Dni=nuevoDniProfesor).where(Profesor.Id == idProfesor).execute()
                            print("El dni del profesor ha sido modificado correctamente")
                            modificado = True
                        else:
                            print("Has cancelado la modificacion del DNI del profesor")
                    except IntegrityError as e:
                        if "Duplicate entry" in str(e):
                            print("Ya existe un profesor con el mismo DNI.")
                        else:
                            print("Error al modificar el DNI del profesor")
                else:
                    print("El dni debe esta formado por 8 digitos y 1 letra")

            elif(opcion=="2"):

                nuevoNombreProfesor = input("Introduce nuevo nombre del profesor: ").strip()
                if(nuevoNombreProfesor != ""):
                    try:
                        if(confirmacion("Estas seguro de que deseas modificar el nombre del profesor? (S/N): ")):
                            Profesor.update(Nombre=nuevoNombreProfesor).where(Profesor.Id == idProfesor).execute()
                            print("El nombre del profesor ha sido modificado correctamente")
                            modificado = True
                        else:
                            print("Has cancelado la modificacion del Nombre del profesor")
                    except:
                        print("Error al modificar el Nombre del profesor")
                else:
                    print("El nombre no puede estar vacio")

            elif(opcion=="3"):

                nuevaDireccionProfesor = input("Introduce nueva direccion del profesor: ").strip()
                if(nuevaDireccionProfesor != ""):
                    try:
                        if(confirmacion("Estas seguro de que deseas modificar la direccion del profesor? (S/N): ")):
                            Profesor.update(Direccion=nuevaDireccionProfesor).where(Profesor.Id == idProfesor).execute()
                            print("La direccion del profesor ha sido modificada correctamente")
                            modificado = True
                        else:
                            print("Has cancelado la modificacion de la Direccion del profesor")
                    except:
                        print("Error al modificar la Direccion del profesor")
                else:
                    print("La direccion no puede estar vacia")

            elif(opcion=="4"):

                nuevoTelefonoProfesor = input("Introduce nuevo telefono del profesor: ").strip()
                if(nuevoTelefonoProfesor.isdigit() and len(nuevoTelefonoProfesor)==9):
                    try:
                        if(confirmacion("Estas seguro de que deseas modificar el telefono del profesor? (S/N): ")):
                            Profesor.update(Telefono=nuevoTelefonoProfesor).where(Profesor.Id == idProfesor).execute()
                            print("El telefono del profesor ha sido modificado correctamente")
                            modificado = True
                        else:
                            print("Has cancelado la modificacion del Telefono del profesor")
                    except:
                        print("Error al modificar el Telefono del profesor")
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

def busquedaProfesor(profesorUnico = False):

    """
    Busca un profesor mediante cualquier atributo del mismo, si es localizado se devuelve el id 
    pera poder gestionarlo en otros metodos

    """

    print("--- Busqueda Profesor ---")

    query = None
    idProfesor = -1
    finBusqueda = False

    while(not finBusqueda):
        opcion = menuAtributos()

        if(opcion=="1"):

            dniProfesor = input("Introduce dni del profesor a buscar: ").strip()
            if(len(dniProfesor)==9 and dniProfesor[8:].isdigit and dniProfesor[8:].isalpha):
                try:
                    query = Profesor.select().where(Profesor.Dni == dniProfesor)
                except DoesNotExist:
                    print("No hay profesores con ese Dni")
            else:
                print("El dni debe esta formado por 8 digitos y 1 letra")

        elif(opcion=="2"):

            nombreProfesor = input("Introduce nombre del profesor a buscar: ").strip()
            if(nombreProfesor != ""):
                try:
                    query = Profesor.select().where(Profesor.Nombre == nombreProfesor)
                except DoesNotExist:
                    print("No hay profesores con ese Nombre")
            else:
                print("El nombre no puede estar vacio")

        elif(opcion=="3"):

            direccionProfesor = input("Introduce direccion del profesor a buscar").strip()
            if(direccionProfesor != ""):
                try:
                    query = Profesor.select().where(Profesor.Direccion == direccionProfesor)
                except DoesNotExist:
                    print("No hay profesores con esa Direccion")
            else:
                print("La direccion no puede estar vacia")

        elif(opcion=="4"):

            telefonoProfesor = input("Introduce telefono del profesor a buscar: ").strip()
            if(telefonoProfesor.isdigit() and len(telefonoProfesor)==9):
                try:
                    query = Profesor.select().where(Profesor.Telefono == telefonoProfesor)
                except DoesNotExist:
                    print("No hay profesores con ese Telefono")
            else:
                print("El telefono debe tener una longitud de 9 digitos")

        elif(opcion=="0"):
            finBusqueda = True
            print("Fin busqueda Profesor")
        else:
            print("Opcion no valida")

        if(not finBusqueda):
            if (query is not None):
                cantidadResultados = query.count()
                
            print("--- Resultado de la Busqueda ---")
            for p in query:
                print("Id_Profesor:"+str(p.Id)+"\n"
                      "Dni:"+p.Dni+"\n"
                      "Nombre:"+p.Nombre+"\n"
                      "Direccion:"+p.Direccion+"\n"
                      "Telefono:"+p.Telefono+"\n"
                      "--------------------------------\n")

            if(cantidadResultados > 1 and profesorUnico):
                finProfesorUnico = False
                while(not finProfesorUnico):
                    idProfesorBuscar = input("Introduce el id del profesor a elegir: ")
                    if(idProfesorBuscar.isdigit()):
                        idEncontrado = False
                        for profesor in query:
                            if (profesor.Id == int(idProfesorBuscar)):
                                idEncontrado = True
                                finProfesorUnico = True
                                finBusqueda = True
                                idProfesor = idProfesorBuscar
                        
                        if (not idEncontrado):
                            print("No existe ningun profesor con ese id")
                    else:
                        print("Tienes que insertar un numero")
            elif(cantidadResultados==1):
                finBusqueda = True
                idProfesor = query[0].Id
            elif(cantidadResultados==0):
                if(not confirmacion("No se han encontrado resultados. Deseas buscar de nuevo? (S/N): ")):
                    finBusqueda = True
    return idProfesor


def mostrarTodosProfesores():

    """
    Muestra todos los profesores que haya en la tabla Profesores

    """

    print("--- Mostrar Todos los Profesores ---")

    try:
        profesores = Profesor.select()

        if(len(profesores)==0):
            print("No hay profesores registrados")

        for p in profesores:
            print("Id_Profesor:"+str(p.Id)+"\n"
                    "Dni:"+p.Dni+"\n"
                    "Nombre:"+p.Nombre+"\n"
                    "Direccion:"+p.Direccion+"\n"
                    "Telefono:"+p.Telefono+"\n"
                    "--------------------------------\n")
    except:
        print("No se han podido mostrar todos los profesores")

def menuAtributos():

    """
    Menu de atributos del profesor entre los que se pueden elegir

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

def menuProfesores():

    """
    Menu de profesores donde se pueden elegir las diferentes operaciones de gestion relacionados con el mismo
    Se pedira una opcion para entrar en alguno de los submenus, si insertas 0, sale al menuPrincipal

    """

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
            insertarProfesor()
        elif(opcion=="2"):
            eliminarProfesor()
        elif(opcion=="3"):
            modificarProfesor()
        elif(opcion=="4"):
            busquedaProfesor()
        elif(opcion=="5"):
            mostrarTodosProfesores()
        elif(opcion=="0"):
            finMenuProfesor = True
        else:
            print("Opcion no valida")