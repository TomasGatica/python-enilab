#   Input/Output IO
#
#   función input()
print("Dime lo que sea ...")
lo_que_sea = input()
print("Hmm...", lo_que_sea, "...¿Eso es todo?")
#   La func input puede imprimir en pantalla sin usar print
lo_que_sea = input("Dime lo que sea ... ")
print("Hmm...", lo_que_sea, "...¿Eso es todo?")
#  
#   El resultado de la función input() ES UNA CADENA
#
#   Conversiones de tipos 
#   float(String) intentará transformar String a un número flotante
#   int(String) same
#   En caso de que no puedan, el programa falla.
#
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: ", (cateto_a**2 + cateto_b**2) ** .5)
#   No maneja excepciones por tipo de datos
#
#   Operadores de Cadenas
#   + al ser aplicado a dos cadenas se transforma en un concatenador
#   string + string
#   NO SE PUEDEN MEZCLAR TIPOS DE DATOS, ambos deben ser cadenas de char
f_name=input("¿Me puedes decir tu nombre? ")
l_name=input("¿Me puedes decir tu apellido? ")
print("...gracias")
print("\nTu nombre es " + f_name + " " + l_name + ".")
#
#   Operador de REPLICACIÓN:
#   El signo * asterisco cuando es aplicado a una cadena y un numero (o viceversa)
#   se convierte en replicador
#   String * number
#   number * string
print("James"*3)    #   $ JamesJamesJames
print(3*"an")   #   $ ananan
print(5*"2")    #   $ 22222
#   Numeros menores o iguales a 0 producen cadenas vacías
#
#   Conversión de tipos STR:
#   De un número a una cadena usamos str(number)