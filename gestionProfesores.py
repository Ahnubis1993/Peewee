from Utilidades import confirmacion


def insertarProfesor(conexionBBDD):
    print("--- Alta Profesor ---")
    
    intentos = 5
    fin = False
    
    while(fin is False and intentos>0):
        dni = input("Introduce Dni Profesor: ").strip()
        if(len(dni)==9 and dni[8:].isdigit and dni[8:].isalpha): 
            fin = True   
            print("Dni correcto")
        else:
            print("Dni no valido")
        intentos -= 1 
    
    if(fin):
        fin = False
        intentos = 5
        
        while(fin is False and intentos>0):
            nombre = input("Introduce Nombre Profesor: ").strip()
            if(nombre != ""): 
                fin = True   
                print("Nombre correcto")
            else:
                print("El nombre no puede estar vacio")
            intentos -= 1 

    if(fin):
        fin = False
        intentos = 5
        
        while(fin is False and intentos>0):
            direccion = input("Introduce Direccion Profesor: ").strip()
            if(direccion != ""): 
                fin = True   
                print("Direccion correcta")
            else:
                print("La direccion no puede estar vacia")
            intentos -= 1    

    if(fin):
        fin = False
        intentos = 5
        
        while(fin is False and intentos>0):
            telefono = input("Introduce Telefono Profesor: ").strip()
            if(telefono.isdigit() and len(telefono)==9): 
                fin = True   
                print("Telefono correcto")
            else:
                print("El telefono no valido")
            intentos -= 1 
                      
    if(fin):
        try:
            cursor = conexionBBDD.cursor()
            cursor.execute("INSERT INTO Profesores (dni, nombre, direccion, telefono) VALUES (%s, %s, %s, %s)",
                           (dni, nombre, direccion, telefono))
            conexionBBDD.commit()
            if(not confirmacion("Alta realizada correctamente. Deseas introducir otro profesor?")):
                fin = True
            print("Fin alta Profesor")
            
        except:
            print("Profesor no dado de alta, fallo en la sentencia Insert sql")
        finally:
            cursor.close()

    else:
        if(not confirmacion("No se ha realizado el alta. Deseas introducir un profesor? (S/N): ")):
            fin = True
            print("Fin alta Profesor")
            
def eliminarProfesor(conexionBBDD):
    print("--- Baja Profesor ---")
    idProfesor = busquedaProfesor(conexionBBDD)
    if(idProfesor != -1):
        try:
            cursor = conexionBBDD.cursor()
            cursor.execute("DELETE FROM Profesores WHERE Id=%s",(idProfesor))
            print("Profesor borrado correctamente\n")
            conexionBBDD.commit()
        except:
            print("Consulta de borrado Profesor no valida")
        finally:
            cursor.close()
    else:
        print("No hay resultados de busqueda. Fin baja profesor")
    
def modificarProfesor(conexionBBDD):
    print("SQL UPDATE") 
    
def busquedaProfesor(conexionBBDD):
    print("--- Busqueda Profesor ---")
    
    id = -1
    finBusqueda = False
    
    while(finBusqueda is False):
        opcion = menuAtributos()
        
        if(opcion=="1"):
            dni = input("Introduce Dni a buscar: ").strip()
            if(len(dni)==9 and dni[8:].isdigit and dni[8:].isalpha):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Dni='"+dni+"'")
                except:
                    print("Consulta por Dni no valida")
            else:
                print("Dni no valido")
        elif(opcion=="2"):
            nombre = input("Introduce Nombre a buscar: ").strip()
            if(nombre != ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Nombre='"+nombre+"'")
                except:
                    print("Consulta por Nombre no valida")
            else:
                print("El nombre no puede estar vacio")
            
        elif(opcion=="3"):
            direccion = input("Introduce Direccion a buscar").strip()
            if(direccion != ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Direccion='"+direccion+"'")
                except:
                    print("Consulta por Direccion no valida")
            else:
                print("La direccion no puede estar vacia")
        
        elif(opcion=="4"):
            telefono = input("Introduce Telefono a buscar: ").strip()
            if(telefono.isdigit() and len(telefono)==9):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Profesores WHERE Telefono='"+telefono+"'")
                except:
                    print("Consulta por Telefono no valida")
            else:
                print("Telefono no valido")
            
        elif(opcion=="0"):
            finBusqueda = True
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
                        idProfesorEncontrado = [filas for f in filas if(f[0]==int(idProfesor))]
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
    print("--- Mostrar Todos ---")
    
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
    fin = False
    while(not fin):
        print("Elige un atributo de los siguientes: ")
        print("--- Atributos ---")
        print("1 - Dni")
        print("2 - Nombre")
        print("3 - Direccion")
        print("4 - Telefono")
        print("0 - Salir")
        opcion = input("Introduce una opcion: ")
        if(opcion.isdigit() and 0 <= int(opcion) <=4):
            fin = True          
        else:
            print("Opcion no valida")
    return opcion
    
def menuProfesores(conexionBBDD):
    
    finMenuProfesor = False
    
    while(finMenuProfesor is False):
        
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
            busquedaProfesor(conexionBBDD)
        elif(opcion=="4"):
            busquedaProfesor(conexionBBDD)
        elif(opcion=="5"):
            mostrarTodosProfesores(conexionBBDD)
        elif(opcion=="0"):
            finMenuProfesor = True
            print("Regresando a Menu Principal. Fin Menu Profesores")
        else:
            print("Opcion incorrecta")
       