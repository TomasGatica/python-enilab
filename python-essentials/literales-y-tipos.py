#   Literals - Literales en python.
#   Utilizamos literales para codificar datos y colocarlos en el código.
#   
print("2")
print(2)
# print(c)
#   Ambas funciones imprimen una salida similar pero no igual
#   "2" es una cadena y 2 es un literal de tipo entero, pero c no.
#   Python posee a grandes rasgos, enteros y de coma flotante.
#   int, float
#   Es muy importante recalcar estas diferencias del lenguaje ya que 
#   representan la forma en que luego son almacenadas las variables y los datos en memoria.
print(1000)
print(1_000)    #   Ambos son los mismo
#   Octales y Hexadecimales
print(0o123)    #   Octal
print(0x123)    #   Hex
#   Flotantes como:
print(.4)
print(2.)   #   Permitido para flotantes
#   Notación científica: 
#   usando la letra e
#   Los textos emplean la abreviación 3x10⁽⁸⁾
#   La base (primer num) puede ser entero o flotante
print(3E8)  #   Puede ser mayus o minus.
#   Por otro lado python puede elegir una notación diferentes en los Outputs
#   por ejemplo:
print(0.0000000000000000000001)
#   Output: 1e-22 
#   Python elige la presentación más corta

#   Cadenas de caracteres
print("I'm your father")
print('I\'m your father')
#   Recordar los carácteres de escape
#   También, las cadenas pueden estar vacías, una cadena vacía
#   sigue siendo una cadena.
#   ''  ""
#   
#   Literales BOOLEANOS
#   veracidad.
print(True < False)
print(True > False)
#   
#   Finalmente exite un literal en Python llamado None. Objeto de NoneType.
#   Utilizado para representar la ausencia de un valor.