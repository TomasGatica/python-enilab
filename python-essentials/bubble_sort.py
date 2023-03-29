#   Implementación del bubble sort 
#   La lista la podemos ordenar de dos maneras
#   1. ascendente (no descendente) - si en cada par de elementos adyacentes,
#   el primer elemento no es mayor que el segundo.
#   2. descendente (no ascendente) - si en cada par de elementos adyacentes,
#   el primer elemento no es menor que el segundo.
#   Ejemplo en el diagrama bubble_sort.drawio

#   Primera vista
mi_lista = [8, 10, 6, 2, 4] # Lista a ordenar
print(len(mi_lista))
for i in range(len(mi_lista) - 1): # largo de la lista - 1
    #   Esto es porque el ultimo elemento no tiene otro adyacente para comparar
    #   y porque los elementos de la lista son 5 un pero el range cuenta desde 0 y len cuenta desde 1
    if mi_lista[i] > mi_lista[i + 1]:   # si el elemento al que apunta
        #   el index actual es mayor que el siguiente elemento indx+1
        #   realizamos el intercambio en la siguiente linea
        mi_lista[i], mi_lista[i + 1] = mi_lista[i + 1], mi_lista[i] #  Intercambio
print(mi_lista)
#   Si imprimimos la lista, solo habremos cambiando un elemento.

#   Segunda vista, incorpora la comparación de todos los elementos.
mi_lista2 = [8, 10, 6, 2, 4]
intercambiado = True # set in true nos permite entrar al bucle while

while intercambiado:    # True
    intercambiado = False   # switch to false
    for i in range(len(mi_lista2) - 1):
        if mi_lista2[i] > mi_lista2[i + 1]:
            intercambiado = True  # ¡ocurrió el intercambio!
            mi_lista2[i], mi_lista2[i + 1] = mi_lista2[i + 1], mi_lista2[i] # pasamos al sig indx
            print(mi_lista2) # Nos permite ver como va iterando el while hasta que no tenga mas 
            # intercambios, por lo que al final, queda en false y sale del bucle
print(mi_lista2)

#   Tercera vista, interactiva
mi_lista3 = []
intercambiado3 = True
num = int(input("Ingrsa cuantos elementos quieres ordenar: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    mi_lista3.append(val)

while intercambiado3:    # True
    intercambiado3 = False   # switch to false
    for i in range(len(mi_lista3) - 1):
        if mi_lista3[i] > mi_lista3[i + 1]:
            intercambiado3 = True  # ¡ocurrió el intercambio!
            mi_lista3[i], mi_lista3[i + 1] = mi_lista3[i + 1], mi_lista3[i] # pasamos al sig indx
            print(mi_lista3) # Nos permite ver como va iterando el while hasta que no tenga mas 
            # intercambios, por lo que al final, queda en false y sale del bucle
print(mi_lista3)