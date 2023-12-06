
def insertarProfesor():
    print("SQL INSERT")

def eliminarProfesor():
    print("SQL DELETE")
    
def modificarProfesor():
    print("SQL UPDATE") 
    
def busquedaProfesor():
    print("SQL SELECT")

def mostrarTodosProfesores():
    print("SQL SELECT")
    
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
            insertarProfesor()
        elif(opcion=="2"):
            eliminarProfesor()
        elif(opcion=="3"):
            busquedaProfesor()
        elif(opcion=="4"):
            busquedaProfesor()
        elif(opcion=="5"):
            mostrarTodosProfesores()
        elif(opcion=="0"):
            finMenuProfesor = True
            print("Regresando a Menu Principal. Fin Menu Profesores")
        else:
            print("Opcion incorrecta")
       