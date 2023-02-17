#  Crear una app que permita ingresar el nombre y las 3 notas  
#  de los N alumnos de un curso.
#  La app debe calcular e imprimir:
#   
#   * Listado con el nombre, las notas, el promedio, y la situación
#     final del alumno
#  
#   Condición: Si el promedio es igual o mayor a 4 la situación 
#              es aprobado, en caso contrario es reprobado.
#
#  * Cantidad de alumnos aprobados
#  * Listado de alumnos reprobados
#  * El/los alumnos con el promedio más alto
#  * Permitir búsqueda por nombre
#  
#  


def menu_principal():
    # Interfaz de acceso a las funciones principales de la aplicación
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("================== App alumnos de un curso ==================")
            print("================== Menú principal ==================")
            print("Que acción desea ejecutar? (tipee el número de la op.)")
            print("1. Ingresar alumnos")
            print("2. Listar todos los alumnos y sus datos")
            print("3. Alumnos aprobados")
            print("4. Lista de alumnos aprobados")
            print("5. Alumno(s) con promedio más alto")
            print("6. Buscar alumno por nombre")
            print("7. Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))
            
            if opcion < 1 or opcion > 7:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 7:
                continuar = False
                print("Gracias por su timepo, vuelva pronto!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)
                
def ejecutarOpcion(opcion):

    if opcion == 1:
        try:
            ingresar.alumnos()
        except:
            print("Ocurrió un error...")
    if opcion == 2:
        try: 
            listar_alumnos()
        except:
            print("Ocurrió un error...")

menu_principal()