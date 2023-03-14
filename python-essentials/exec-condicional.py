#   Condiciones y ejecución condicional
#   Sentencia if
#   if , expresión cuyo valor se interpreta en términos 
#   de True o False.
contador_ovejas = 0   # cambio a menor exec alimentar ovejas
if contador_ovejas >= 120:
    print("hacer cama")
    print("tomar ducha")
    print("domir")
print("alimentar ovejas")#  Notar que cada print podría ser una func

#   Condiciones if-else
#   if (condición):
#       instrucción
#   else:
#       instrucción
#   La ejecución de bloques if-else dependen de la evaluación de la condición
#   en True o False.

#   Condición elif
#   elif condición:
if (contador_ovejas == 0):
    print("True, contador igual a 0")
elif (contador_ovejas != 0):
    print("True, también quiero evaluar elif")
else:
    print("False, salió todo mal")

#   La principal diferencia de usar bloque if-elif-else
#   con un if-if-else es que al evaluar en if-if siempre todas las
#   expresiones son evaluadas.
#   el elif va ligado al valor del if o elif que le preceda (antes)
#   y el else siempre se ejecuta cuando nada de lo demás se cumple


#   Bucles
#   while ejecuta el bloque mientras la condición se evalúa 
#   como True

#   Bucle for
#   for i in range(x):
#       hacer_algo()
#   cualquier variable dsp de for es la variable de control del bucle
#   recordar que range empieza desde 0

meses = int(input("¿Cuantos meses tiene su calendario?: "))
dias = int(input("Cuantos días tiene su calendario?: "))
for i in range(meses):
    print("Mes ", i+1)
    for d in range(dias):
        print(d+1, end="-") 
    print()
#   
#   La función range puede recibir un primer argumento como el valor 
#   inicial y recordar que la variable final considera el entero
#   previo al valor final ("99 en vez de 100")
#   
#   La variable range puede recibir un tercer argumento, que 
#   indica un valor de incremento
for i in range(1,10,3):
    print("El valor de i es ", i)
#   $ i -> 1
#   $ i -> 4
#   $ i -> 7
#   Como podemos observar, comenzando la primera vuelta del bucle
#   pasa tomar el incremento de 3 para el valor de i
#   
#   Range toma valores en orden ascendente
import time

for segundos in range(1,6):
    print(segundos, "Mississippi")
    time.sleep(1)   #   Simula el paso de 1 seg
print("Listos o no ahí voy!")

#
#   
#   Sentencias break y continue
#
#   Ejemplo de muestra
print("Instrucción break: ")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle")
#
#   Con esto, entendemos que la función break es capaz de salir de un
#   bucle, terminando su operación
#   y comienza a ejecutar la instrucción más cercana
#   dsp del bucle
#   
#   continue 
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle")
print("Fuera del bucle")
#
#   Esta sentencia se comporta como si el programa llegara al final
#   del cuerpo del bucle (OJO NO A SU FIN EXE) por lo que la sig 
#   vuelta del bucle comienza y la condición se prueba de inmediato
#
#   Devorador de vocales
palabra_ingresada = input("Ingresa tu palabra ")
palabra_ingresada = palabra_ingresada.upper()
for letra in palabra_ingresada:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra)
    #   else:
    #       palabra_sin_vocales += letra
    #print(palabra_sin_vocales)
    
    #
#   Hipotesis de Collatz
#   1. Toma cualquier numero entero que no sea negativo y no sea 0
#   asignandole el nombre de c0.
#   2. Si es par evalúa de nuevo c0 como c0 / 2
#   3. Si es impar, evaluar un nuevo c0 como 3 x c0 + 1
#   4. si c0 != 1 salta al punto 2

c0 = int(input("Igresa c0: "))
if c0 > 1:  # 1.
    pasos = 0   # contador pasos
    while c0 != 1:  #   4.
        if c0 % 2 != 0: # 3.
            cnew = 3 * c0 +1    # 3.
        else:
            cnew = c0 // 2  # 2. 
        print(c0)
        c0 = cnew
        pasos += 1
    print("Pasos = ", pasos)
else:
    print("Valor de c0 incorrecto ")
    
#
#   
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

#
#  
print("\n")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")