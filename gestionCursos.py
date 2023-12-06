
def insertarCurso():
    print("SQL INSERT")

def eliminarCursor():
    print("SQL DELETE")
    
def modificarCurso():
    print("SQL UPDATE") 
    
def busquedaCurso():
    print("SQL SELECT")

def mostrarTodosCursos():
    print("SQL SELECT")
    
def menuCursos(conexionBBDD):
    
    finMenuCurso = False
    
    while(finMenuCurso is False):
        
        print("--- Menu Cursos ---")
        print("1 - Alta")
        print("2 - Baja")
        print("3 - Modificar")
        print("4 - Busqueda")
        print("5 - Mostrar Todos")
        print("0 - Salir")
        opcion = input("Introduce una Opcion: ").strip()
        
        if(opcion=="1"):
            insertarCurso()
        elif(opcion=="2"):
            eliminarCursor()
        elif(opcion=="3"):
            busquedaCurso()
        elif(opcion=="4"):
            busquedaCurso()
        elif(opcion=="5"):
            mostrarTodosCursos()
        elif(opcion=="0"):
            finMenuCurso = True
            print("Regresando a Menu Principal. Fin Menu Cursos")
        else:
            print("Opcion incorrecta")