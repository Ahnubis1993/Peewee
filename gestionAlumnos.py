
def insertarAlumno():
    print("SQL INSERT")

def eliminarAlumno():
    print("SQL DELETE")
    
def modificarAlumno():
    print("SQL UPDATE") 
    
def busquedaAlumno():
    print("SQL SELECT")

def mostrarTodosAlumnos():
    print("SQL SELECT")
    
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
            insertarAlumno()
        elif(opcion=="2"):
            eliminarAlumno()
        elif(opcion=="3"):
            busquedaAlumno()
        elif(opcion=="4"):
            busquedaAlumno()
        elif(opcion=="5"):
            mostrarTodosAlumnos()
        elif(opcion=="0"):
            finMenuAlumno = True
            print("Regresando a Menu Principal. Fin Menu Alumnos")
        else:
            print("Opcion incorrecta")