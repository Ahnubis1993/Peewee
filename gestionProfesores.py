from Utilidades import confirmacion


def insertarProfesor(conexionBBDD):
    print("--- Alta Profesor ---")
    
    intentos = 5
    correcto = False
    
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
        try:
            cursor = conexionBBDD.cursor()
            cursor.execute("INSERT INTO Profesores (dni, nombre, direccion, telefono) VALUES (%s, %s, %s, %s)",
                           (dniProfesor.upper(), nombreProfesor, direccionProfesor, telefonoProfesor))
            conexionBBDD.commit()
            if(not confirmacion("El alta del profesor se ha realizado correctamente. Deseas introducir otro profesor? (S/N): ")):
                correcto = True
                print("Fin alta Profesor")
            
        except:
            print("Profesor no dado de alta, fallo al introducir el profesor en la base de datos")
        finally:
            if (cursor is not None):
                cursor.close()

    else:
        if(not confirmacion("El alta del profesor no se ha realizado correctamente. Deseas introducir un profesor? (S/N): ")):
            correcto = True
            print("Fin alta Profesor")
            
def eliminarProfesor(conexionBBDD):
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
            cursor.close()
    else:
        print("No hay resultados de busqueda. Fin baja profesor")
    
def modificarProfesor(conexionBBDD):
    print("--- Modificacion Profesor ---")
    
    idProfesor = busquedaProfesor(conexionBBDD)
    
    finModificacionProfesor = False
    
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
                            cursor.close()
                            print("El dni del profesor ha sido modificado correctamente")
                        else:
                            print("Has cancelado la modificacion")
                    except:
                        print("Consulta por Dni no valida")
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
                            cursor.close()
                            print("El nombre del profesor ha sido modificado correctamente")
                        else:
                            print("Has cancelado la modificacion")
                    except:
                        print("Consulta por Nombre no valida")
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
                            cursor.close()
                            print("La direccion del profesor ha sido modificada correctamente")
                        else:
                            print("Has cancelado la modificacion")
                    except:
                        print("Consulta por Direccion no valida")
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
                            cursor.close() 
                            print("El telefono del profesor ha sido modificado correctamente")  
                        else:
                            print("Has cancelado la modificacion")                                        
                    except:
                        print("Consulta por Telefono no valida")
                else:
                    print("El telefono debe tener una longitud de 9 digitos")
                
            elif(opcion=="0"):
                finModificacionProfesor = True
                print("Fin busqueda Profesor")
            else:
                print("Opcion no valida")
                
                #TODO hay que ver como se captura para pedir al USU si quieres volver a modificar
    else:
        print("No hay resultados de busqueda. Fin modificar profesor")
        
def busquedaProfesor(conexionBBDD):
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
                    cursor.close()
                except:
                    #TODO
                    print("Consulta por Dni no valida")
            else:
                print("El dni debe esta formado por 8 digitos y 1 letra")
        elif(opcion=="2"):
            nombreProfesor = input("Introduce nombre del profesor a buscar: ").strip()
            if(nombreProfesor != ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Nombre=%s", (nombreProfesor))
                    filasTablaProfesor = cursor.fetchall()
                    cursor.close()
                except:
                    #TODO
                    print("Consulta por Nombre no valida")
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
                    #TODO
                    print("Consulta por Direccion no valida")
            else:
                print("La direccion no puede estar vacia")
        
        elif(opcion=="4"):
            telefonoProfesor = input("Introduce telefono del profesor a buscar: ").strip()
            if(telefonoProfesor.isdigit() and len(telefonoProfesor)==9):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Telefono=%s", (telefonoProfesor))
                    filasTablaProfesor = cursor.fetchall()
                    cursor.close()
                except:
                    #TODO
                    print("Consulta por Telefono no valida")
            else:
                print("El telefono debe tener una longitud de 9 digitos")
            
        elif(opcion=="0"):
            finBusquedaProfesor = True
            print("Fin busqueda Profesor")
        else:
            print("Opcion no valida")
            
        if(finBusqueda is False):
            print("--- Resultado ---")
            filas = cursor.fetchall()
            cursor.close()
            
            for f in filas:
                print("Id_Profesor:"+str(f[0])+"\n"
                      "Dni:"+f[1]+"\n"
                      "Nombre:"+f[2]+"\n"
                      "Direccion:"+f[3]+"\n"
                      "Telefono:"+str(f[4])+"\n")
            
            if(len(filas)>1):
                finIdProfesor = False
                while(finIdProfesor is False):
                    idProfesor = input("Introduce el id del profesor a elegir")
                    if(idProfesor.isdigit()):
                        idProfesorEncontrado = [fila for fila in filas if(fila[0]==int(idProfesor))]
                        if(idProfesorEncontrado):
                            finBusqueda = True
                            id = idProfesorEncontrado[0]
                    else:
                        print("Tienes que insertar un numero")
            elif(len(filas)==1):
                finBusqueda = True
                id = filas[0][0]
                
            else:
                if(not confirmacion("No se han encontrado resultados. Deseas buscar de nuevo? (S/N): ")):
                    finBusqueda = True
    return id
    

def mostrarTodosProfesores(conexionBBDD):
    print("--- Mostrar Todos los Profesores ---")
    
    try:
        cursor=conexionBBDD.cursor()
        cursor.execute("SELECT * FROM Profesores")
        filas = cursor.fetchall()
        
        for f in filas:
            print("Id_Profesor:"+str(f[0])+"\n"
                    "Dni:"+f[1]+"\n"
                    "Nombre:"+f[2]+"\n"
                    "Direccion:"+f[3]+"\n"
                    "Telefono:"+str(f[4])+"\n")
            
    except:
        print("No se han podido mostrar todos los profesores")
    
def menuAtributos(): 
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
            print("Opcion incorrecta")
       