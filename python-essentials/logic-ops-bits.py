#   and, or
#   conjuncion y disyuncion
#   Estos son operadores binarios
#   Tienen una tabla de verdad respecto a sus valores booleanos
#   Lo mismo con el not operator
#       not (p and q) == (not p) or (not q)
#       not (p or q) == (not p) and (not q)
#   Expresiones logicas
#   Valores lógicos vs bits individuales
#   Los op logicos toma sus args como un todo independiente
#   de cuantos bits contengan.
#   Los operadores conocen dos valores
#   0 cuando todos los bits se restablecen
#   1 (no cero) cuando se establece al menos 1 bit

#   Operadores bit a bit
#   Permiten manipular bits de datos individuales
#   a estos se les añade un operador extra, XOR
#   que es un or exclusivo
#   & (ampersand) ‒ conjunción a nivel de bits;
#   | (barra vertical) - disyunción a nivel de bits;
#   ~ (tilde) - negación a nivel de bits;
#   ^ (signo de intercalación) - o exclusivo a nivel de bits (xor).
#
#   Los operadores deben ser enteros cuando usamos op bit a bit
#   La diferencia entre los operadores lógicos y de bits es que los
#   lógicos no penetran a nivel de bits de su argumento. Solo les interesa
#   el valor entero final
#   Para plasmarlo mejor.
#   Supongamos que tenemos dos variables i = 5 , j = 22
#   al operar log = i and j , la evaluacion es:
#       como ambos valores no son 0 se toman como un True
#       ya que su representacion en binario no es 0
#   
#   En cambio, cuando operamos con & opera a nivel de bits,
#   por lo que su evaluacion finalizara como un 00110 = 6 en binario
#   lo mismo con el not, transforma el todo en un False
#   en cambio ~i cambia el valor en bits 0a1 y 1a0 por lo que su valor
#   final sera otro numero en binario i.e = 00000001111 a 1111110000.
#   Tambien se pueden usar de forma abreviada. 

#   1. Python es compatible con los siguientes operadores lógicos:
#   
#   and → si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, (True and True) es True.
#   or → si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, (True or False) es True.
#   not → devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, not True es False.
#   2. Puedes utilizar operadores bit a bit para manipular bits de datos individuales. Los siguientes datos de muestra:
#   
#   x = 15, el cual es 0000 1111 en binario,
#   y = 16, el cual es 0001 0000 en binario.
#   Se utilizarán para ilustrar el significado de operadores bit a bit en Python. Analiza los ejemplos a continuación:
#   
#   & hace un bit a bit and (y), por ejemplo, x & y = 0, el cual es 0000 0000 en binario,
#   | hace un bit a bit or (o), por ejemplo, x | y = 31, el cual es 0001 1111 en binario,
#   ˜ hace un bit a bit not (no), por ejemplo, ˜ x = 240*, el cual es 1111 0000 en binario,
#   ^ hace un bit a bit xor, por ejemplo, x ^ y = 31, el cual es 0001 1111 en binario,
#   >> hace un desplazamiento bit a bit a la derecha, por ejemplo, y >> 1 = 8, el cual es 0000 1000 en binario,
#   << hace un desplazamiento bit a bit a la izquierda, por ejemplo, y << 3 = , el cual es 1000 0000 en binario.

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
# $ 0 5 -5 1 1 16
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))
# $ False