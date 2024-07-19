class Punto:
    """Representa un punto en el espacio"""

    def __init__(self, x, y, z):
        """ Método de inicialización de un punto en el espacio, compuesto de
            atributos x, y ,z.
        """
        self.x = x
        self.y = y
        self.z = z

    def mostrar(self):
        """Método que permite mostrar nuestro punto en el espacio"""
        print("Punto ({}, {}, {})".format(self.x, self.y, self.z))


p = Punto(1, 2, 3)
p.mostrar()

class MiClase: 
    """Documentación""" 
    def mi_metodo(self, nombre): 
        print("{}.mi_metodo({})".format(self, nombre))
        
instancia = MiClase() # Creamos una variable para instanciar la clase
instancia.mi_metodo("Tomás") # La variable utiliza mi_metodo completando 
                             # lo requerido por el método de la clase 

class Circulo: 
    """ Clase círculo parametrizada y solo con un método
        a veces llamada ActionClass
    """
    radio = 2
    def perimetro(self):
        return 2 * 3.14 * self.radio

c = Circulo()
print(c.perimetro())
