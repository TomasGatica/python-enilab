
class sucursal:
    
    def __init__(self, nombre_sucursal, direccion, telefono, lista_sucursales):
        self.nombre_sucursal=nombre_sucursal
        self.direccion=direccion
        self.telefono=telefono
        self.lista_sucursales=lista_sucursales
    
    def ingreso_sucursales(self, lista_sucursales):
        
        nombre_sucursal = input("Ingrese el nombre de la sucursal: ")
        direccion = input("Ingresa la direccion: ")   
        telefono = input("Ingresa el telefono: ")
        objeto_sucursal=sucursal(nombre_sucursal,direccion,telefono)
        lista_sucursales.append(objeto_sucursal)
        
class trabajador:
    # Data del trabajador
    rut=""
    nombre_trabajador=""
    telefono_trabajador=""
    cargo=""  
    sueldo=""

    def __init__(self, rut, nombre_trabajador, telefono_trabajador, cargo, sueldo):
        self.rut=rut
        self.nombre_trabajador=nombre_trabajador
        self.telefono_trabajador=telefono_trabajador
        self.cargo=cargo
        self.sueldo=sueldo
    
    def ingreso_trabajadores(self):
        rut = input("Ingresa el rut: ")
        nombre_trabajador = input("Ingresa el nombre: ")
        telefono_trabajador = input("Ingresa el telefono: ")
        cargo = print("Ingresa el cargo: ") 
        while True:
            try:
                sueldo = int(input("Ingresa el sueldo: "))
                break
            except ValueError:
                print("Ingrese un sueldo válido")
        objeto_trabajador=trabajador(rut,nombre_trabajador,telefono_trabajador,cargo,sueldo)
        trabajador.append(objeto_trabajador)


s=sucursal(0,0,0,0)
lista_sucursales=[]


#  def interfaz_inicio():
#      try:
#          while True:
#              print("Gestión de sucursales y trabajadores...")
#              print("A continuación ingrese una sucursal...")
#              sucursal.ingreso_sucursales()
#              print("Ingresa los trabajadores de la sucursal: ")
#              trabajador.ingreso_trabajadores()
#      except:
#          pass

