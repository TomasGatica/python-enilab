# Programa por CLI que permite solicitar un número entre 0 - 99
# para luego pedir al usuario que lo adivine.

#import random
#
#numero = random.randint(0, 100)
#primera parte original 1.1
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


# FUNCIONES
MIN = 0
MAX = 99
minimo = MIN
maximo = MAX
def pedir_numero(invitacion, minimo=MIN, maximo=MAX):
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + ": "
    while True:
        entrada = input(invitacion)
        try: 
            entrada = int(entrada) 
        except: 
            pass 
        else: 
            if minimo <= entrada <= maximo: 
                break 
    return entrada

#primera parte 
numero = pedir_numero("Introduzca el número a adivinar ")
        
#segunda parte
print("Intente adivinar el número ") 
while True:  # BUCLE 1
    intento = pedir_numero(
        "Adivine el número ", 
        minimo, 
        maximo,
    ) 
    if intento < numero: 
        print("Demasiado pequeño")
        minimo = intento + 1 
    elif intento > numero: 
        print("Demasiado grande")
        maximo = intento - 1 
    else: 
        print("¡Ha ganado!") 
        break  # Bucle 


    
    
    
    
    
    