# Programa CLI que permite solicitar un número entre 0 - 99
# para luego pedir al usuario que lo adivine.

import random

numero = random.randint(0, 100)
#   primera parte original 1.1
#
#print("Introduzca el número a adivinar")
#while True:
#    numero = input("Introduzca un número entre 0 y 99: ")
#    try:
#        numero = int(numero) 
#    except:
#        pass
#    else:
#        if 0 <= numero <= 99:
#            break
#
def pedir_numero():
    while True:
        entrada = input("Introduzca un número entre 0 y 99: \n")
        try: 
            entrada = int(entrada) 
        except: 
            pass 
        else: 
            if 0 <= entrada <= 99: 
                break 
    return entrada

#primera parte 1.2
print("Juego de adivinanzas")
numero = pedir_numero()
        
#segunda parte
print("Intenta adivinar el número") 
while True:  # BUCLE 1 
    while True:  # BUCLE 2
        print("Introduzca un número entre 0 y 99:\n")
        intento = input() 
        try: 
            intento = int(intento) 
        except: 
            pass 
        else: 
            if 0 <= intento <= 99: 
                break  # Bucle 2 
 
    if intento < numero: 
        print("Demasiado pequeño") 
    elif intento > numero: 
        print("Demasiado grande") 
    else: 
        print("¡Ha ganado!") 
        break  # Bucle 1
