# Programa por CLI que permite solicitar un número entre 0 - 99
# para luego pedir al usuario que lo adivine.
import sys


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
            print("Solo estan autorizados los caracteres [0-9] ",
                file=sys.stderr) 
        else: 
            return entrada

#primera parte 
numero = pedir_numero("Introduzca el número a adivinar ")
        
#segunda parte
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


    
    
    
    
    
    