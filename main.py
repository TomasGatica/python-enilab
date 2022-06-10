import sys 

#var inputs
numero1 = input("Ingrese un primer numero: ")
numero2 = input("Ingrese un segundo numero: ")

#func comparar

comparacion = numero1 < numero2
print(numero1, "<", numero2, ":", comparacion)



numero3 = int(input("Ingrese un primer numero: "))
numero4 = int(input("Ingrese un segundo numero: "))

comparacion2 = numero3 < numero4
print(numero3, "<", numero4, ":", comparacion2)

# concatenacion 

variable1 = 'Pantalla'
variable2 = 'Torre'
print(variable1 + variable2) #concatena la cadena sin agregar extras
print(variable1, variable2) #agrega espacio


# mismo valor para varias var's 

variable3 = variable4 = variable5 = 'Algo'



var1 = input("Introduzca un número")
try:
    var1 = int(var1)
except:
    print("La conversión de este número no ha tenido éxito ",
          file=sys.stderr)
    sys.exit()
var2 = input("Introduzca otro número")
try:
    var2 = int(var2)
except:
    print("La conversión de este número no ha tenido éxito ",
          file=sys.stderr)
    sys.exit()


