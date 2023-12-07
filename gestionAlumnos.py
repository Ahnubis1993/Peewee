from Utilidades import confirmacion
from pymysql import IntegrityError
import re

def insertarAlumno(conexionBBDD):
    print("--- Alta Alumno ---")
    
    intentos = 5
    correcto = False
    
    while(not correcto and intentos>0):
        expediente = input("Introduce el Numero de Expediente: ").strip()
        if(expediente != ""): 
            correcto = True   
            print("Expediente valido")
        else:
            print("El expediente no puede estar vacio")
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
        
        while(not correcto and intentos>0):
            apellidos = input("Introduce los apellidos: ").strip()
            if(nombre != ""): 
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
            cursor = conexionBBDD.cursor()
            cursor.execute("INSERT INTO Alumnos (Num_Expediente, nombre, apellidos, telefono, direccion, Fecha_Nacimiento) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (expediente, nombre, apellidos, telefono, direccion, fechaNac))
            conexionBBDD.commit()
            if(not confirmacion("Alta realizada correctamente. Deseas introducir otro alumno? (S/N): ")):
                correcto = True
            print("Fin de alta de alumno")
            
        except IntegrityError as e:
            # Capturar error de integridad de la base de datos
            
            if "Duplicate entry" in str(e):
                print("Ya existe un alumno con el mismo nombre y apellidos.")
            elif "Incorrect date value" in str(e):
                print("La fecha de nacimiento no es correcta. Debe ser yyyy-mm-dd")
            else:
                print("Error al introducir el alumno en la base de datos")
                
        except Exception as e:
            print(f"Alumno no dado de alta, fallo al introducir el alumno en la base de datos\n {e}")
            
        finally:
            if (cursor is not None):
                cursor.close()

    else:
        if(not confirmacion("No se ha realizado el alta. Deseas introducir otro alumno? (S/N): ")):
            correcto = True
            print("Fin de alta de alumno")

def eliminarAlumno(conexionBBDD):
    print("--- Baja Alumno ---")
    expediente = busquedaAlumno(conexionBBDD)
    if(expediente != -1):
        try:
            cursor = conexionBBDD.cursor()
            cursor.execute("DELETE FROM Alumnos WHERE Num_Expediente=%s",(expediente))
            print("Alumno eliminado correctamente\n")
            conexionBBDD.commit()
        except:
            print("Error al eliminar el alumno de la base de datos")
        finally:
            cursor.close()
    else:
        print("No hay resultados de busqueda. Fin de baja de alumno")
    
def modificarAlumno(conexionBBDD):
    print("SQL UPDATE") 
    
def busquedaAlumno(conexionBBDD, alumnoUnico = False):
    print("--- Busqueda Alumno ---")
    
    numExpediente = -1
    finBusqueda = False
    
    while(not finBusqueda):
        opcion = menuAtributos()
        
        if (opcion == "1"):
            expediente = input("Introduce el Numero de Expediente a buscar: ").strip()
            if (expediente != ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Alumnos WHERE Num_Expediente='" + expediente +"'")
                except:
                    print("Consulta por Numero de Expediente no valida")
            else:
                print("No puedes buscar por un Numero de Expediente vacio")
                
        elif (opcion == "2"):
            nombre = input("Introduce el Nombre a buscar: ").strip()
            if(nombre!= ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Alumnos WHERE Nombre='"+nombre+"'")
                except:
                    print("Consulta por Nombre no valida")
            else:
                print("No puedes buscar por un nombre vacio")
                
        elif (opcion == "3"):
            apellidos = input("Introduce los Apellidos a buscar: ").strip()
            if(apellidos!= ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Alumnos WHERE Apellidos='"+apellidos+"'")
                except:
                    print("Consulta por Apellidos no valida")
            else:
                print("No puedes buscar por apellidos vacios")
                
        elif (opcion == "4"):
            telefono = input("Introduce el Telefono a buscar: ").strip()
            if(telefono.isdigit() and len(telefono)==9):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Alumnos WHERE Telefono='"+telefono+"'")
                except:
                    print("Consulta por Telefono no valida")
            else:
                print("Telefono no valido. Deben ser 9 digitos sin espacios.")
                
        elif (opcion == "5"):
            direccion = input("Introduce la direccion a buscar: ").strip()
            if(direccion!= ""):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Alumnos WHERE Direccion='"+direccion+"'")
                except:
                    print("Consulta por Direccion no valida")
            else:
                print("No puedes buscar por una direccion vacia")
                
        elif (opcion == "6"):
            fechaNac = input("Introduce la fecha de nacimiento a buscar (yyyy-mm-dd): ").strip()
            
            if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", fechaNac):
                try:
                    cursor = conexionBBDD.cursor()
                    cursor.execute("SELECT * FROM Alumnos WHERE Fecha_Nacimiento='"+fechaNac+"'")
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
            print("--- Resultado de la Busqueda ---")
            filas = cursor.fetchall()
            cursor.close()
            
            for f in filas:
                print("Numero de expediente:"+str(f[0])+"\n"
                      "Nombre:"+f[1]+"\n"
                      "Apellidos:"+f[2]+"\n"
                      "Telefono:"+f[3]+"\n"
                      "Direccion:"+f[4]+"\n"
                      "Fecha de Nacimiento:"+str(f[5])+"\n"
                      "--------------------------------\n")
            
            if(len(filas)>1 and alumnoUnico):
                finAlumnoUnico = False
                while(not finAlumnoUnico):
                    expediente = input("Introduce el numero de expediente del alumno a elegir")
                    if(expediente.isdigit()):
                        numExpedienteEncontrado = [fila for fila in filas if(fila[0]==int(expediente))]
                        if(numExpedienteEncontrado):
                            finBusqueda = True
                            numExpediente = numExpedienteEncontrado[0]
                    else:
                        print("Tienes que insertar un numero")
            elif(len(filas)==1):
                finBusqueda = True
                numExpediente = filas[0][0]
            else:
                if(not confirmacion("No se han encontrado resultados. Deseas buscar de nuevo? (S/N): ")):
                    finBusqueda = True
    return numExpediente

def mostrarTodos(conexionBBDD):
    print("--- Mostrando todos los alumnos ---")
    try:
        cursor=conexionBBDD.cursor()
        cursor.execute("SELECT * FROM Alumnos")
        filas = cursor.fetchall()
        
        if (len(filas)==0):
            print("No hay alumnos registrados")
        
        for f in filas:
                print("Numero de expediente:"+str(f[0])+"\n"
                      "Nombre:"+f[1]+"\n"
                      "Apellidos:"+f[2]+"\n"
                      "Telefono:"+f[3]+"\n"
                      "Direccion:"+f[4]+"\n"
                      "Fecha de Nacimiento:"+str(f[5])+"\n"
                      "--------------------------------\n")
    except:
        print("No se han podido mostrar todos los alumnos")
    
def menuAtributos(): 
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

def menuAlumnos(conexionBBDD):
    
    finMenuAlumno = False
    
    while(finMenuAlumno is False):
        
        print("--- Menu Alumnos ---")
        print("1 - Alta")
        print("2 - Baja")
        print("3 - Modificar")
        print("4 - Busqueda")
        print("5 - Mostrar Todos")
        print("0 - Salir")
        opcion = input("Introduce una Opcion: ").strip()
        
        if(opcion=="1"):
            insertarAlumno(conexionBBDD)
        elif(opcion=="2"):
            eliminarAlumno(conexionBBDD)
        elif(opcion=="3"):
            busquedaAlumno(conexionBBDD)
        elif(opcion=="4"):
            busquedaAlumno(conexionBBDD)
        elif(opcion=="5"):
            mostrarTodos(conexionBBDD)
        elif(opcion=="0"):
            finMenuAlumno = True
            print("Regresando a Menu Principal. Fin Menu Alumnos")
        else:
            print("Opcion incorrecta")