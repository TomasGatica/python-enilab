#
#   Variables.
var = "3.8.5"
print("Python versión: "+ var)
#   Usando el operador + para concatenar
var = 100
var = 200 + 300
print(var)  #   $ 500
john=3
mary=5
adam=6
print(john, mary, adam, sep=',')
total_apples=john+mary+adam
print("El total de manzanas es: "+str(total_apples))
#   str función toString al concatenar
print("El total de manzanas es:",total_apples)
#   , pasarle otra variable a print
#
#   Operadores abreviados:
#   Mientras que: variable = variable op expresión
#   lo anterior es igual a
#   variable op= expresión
x=2 #   ignore
x = x**2
x **= 2
#   Los dos ultimos son lo mismo.
#
#   Convertidor de millas/kilometros 
#                  kilometros/millas
kilometros = 12.24 
millas = 7.38

millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61

print(millas, "millas son", round(millas_a_kilometros, 2), "Kilómetros")
print(kilometros, "kilómetros son", round(kilometros_a_millas, 2), "Millas")


#   Tipos de datos, variables y operaciones básicas IO

#   las palabras clave van al final
print("La witsi witsi araña", "subió", end=" ", sep="-")
print("La witsi witsi araña", "subió", end=" ")

print("Mi","nombre", "es", sep="_", end="*\n")
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")  #   Comillas en Output.


#   print(sep="&", "fish", "chips") SyntaxError: positional arg keyword

variable_caracter = 'Variable en comilla simple'
VARIABLE_STRING = "Variable en comilla doble"

#   Tipos de datos 
entero = 100    #   integer
coma_flotante = 0.1 #   float
complejos = 1j  #   complejos
print(entero, coma_flotante, complejos)