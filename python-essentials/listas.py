numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.


#   Funciones vs Metodos
#   En palabras sencillas:
#   Un método es propiedad de los datos para los que trabaja
#   mientras que una función es propiedad de todo el código
#   Una función no pertenece a ningún dato, obtiene datos, puede
#   crear nuevos datos y generalmente produce un resultado
#   Un metodo hace todo esto pero tambien puede cambiar el estado
#   de una entidad seleccionada.
#   result = function(arg)
#   result = data.method(arg)
#   
#   list.append(value) toma el valor del arg y lo coloca la final de la lst
#   list.insert(location, value) agrega en lugar y valor
#   my_list = []
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)
print(my_list)
# $[5, 4, 3, 2, 1]
#   Esto sucede porque el metodo insert va a ir desplazando 
#   a la derecha los elementos que se colocan en una misma posición
#   como la pos 0 y el valor iterado por el ciclo for
#
#   Analizando dos implementaciones
my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)
#  
my_list = [10, 1, 8, 3, 5]
total = 0
for i in my_list:
    total += i
print(total)

# Intercambios de orden
variable_1 = 1
variable_2 = 2
variable_1, variable_2 = variable_2, variable_1
#   Si hicieramos una asignación típica como var1 = var2 de inmediato
#   perdemos el valor de var2 si es que queríamos usarlo. 
#   La forma anterior nos permite hacerlo de manera mas sencilla y completa
#   Lo mismo podemos aplicar en las listas
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Los Beatles
# paso 1:
Beatles = []
print("Paso 1:", Beatles)

# paso 2:

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3:
for members in range(2):
    Beatles.append(input("Nuevo miembro de la banda: "))
    # insertamos a Stu Sutcliffe y Pete Best
print("Paso 3:", Beatles)

# paso 4:
del Beatles[-1]
del Beatles[-1]
print("Paso 4:", Beatles)

# paso 5:
Beatles.insert(0, "RingoStarr")
print("Paso 5:", Beatles)
print("Los Fav:",len(Beatles))

#   Resumiendo
#   Recuerda que las listas son una colección ordenada y mutable
my_list = [1, None, True, "Soy una cadena", 256, 0]
#
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)# [1, 6, 2, 3, 4, 5]
del lst[0]# [6, 2, 3, 4, 5]
lst.append(1)# [6, 2, 3, 4, 5, 1]
print(lst)
#
lst = []
del lst
# print(lst)
#   NameError: name lst is not defined

#   Sin embargo recordar que Python como todo lenguaje
#   tiene built-in functions para ayudarnos a realizar estas tareas
my_list2 = [8, 10, 6, 2, 4]
my_list2.sort()
print(my_list2)
my_list2.reverse()
print(my_list2)

#   Algo que distingue las listas de las variables ordinarias:
list_1 = [1] # indx 0 = 1
list_2 = list_1 # copia memory location de la list_1
list_1[0] = 2 # cambiamos el elemento
print(list_2) # $ [2] 
# 
#   El nombre de una variable ordinaria es el nombre de su contenido
#   El nombre de una lista es el nombre de una ubicación de memoria
#   DONDE SE ALMACENA LA LISTA.
#   Por lo tanto, la asignación list_1 = list_2 copia el nombre 
#   del arreglo, no su contenido. Ambas listas identifican la misma 
#   ubicación en memoria, modificar uno afecta al otro
#
#   Para solucionar este problema podemos usar las Slices/Rebanadas o rodajas
#
#   my_list[inicio:fin] NOTA: inicio se considera, pero fin no, por lo que se dice fin-1
#   esto nos permite crear una lista de destino con el contenido
#   copiado
#   Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:] # aqui rebanamos incluyendo todo en la nueva lista
list_1[0] = 2 # vemos que no produce efecto
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # el 3er elemento es 4 pero este no se considera / fin-1
print(new_list)
#   Dejar el inicio vacio toma desde el indx 0 my_list[:end]
#   lo mismo a la inversa my_list[start:]
#
#   Los indices negativos
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
#   La función del() también nos permite eliminar por rebanadas
del my_list[1:3] # OJO que esto no produce una salida nueva.
#   del my_list[:] delete all elements

my_list = [10, 8, 6, 4, 2]
del my_list
# print(my_list)
#   Elimina la lista, NO SU CONTENIDO
#   uncomm print de arriba
#   $ NameError: name my_list is not defined

# Operadores in y not in 
#
#   Capaces de verificar si un valor específico está almacenado
#   dentro de la lista o no. 
#   in verifica si un elemento está almacenado en algun lado de la lista
#   devuelve True si es el caso.
#   not in por el contrario compruena si no está en la lista, devuelve
#   True si es el caso.

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


#   Algunos programas con listas
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#   Encontrando la ubicacion de un elemento dentro de una lista
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
if found:
    print("Elemento encontrado en el índice: ", i)
else:
    print("No encontramos nada")
    
#   Loteríaaaaa. Imagina que elijes tus números de la suerte
#   los almacenaremos en una lista.
#   En otra lista tendremos los números ganadores.
#   Y tendremos una variable del tipo contador para verificar
#   las veces que le "achuntamos al número"
#   mis_numeros = [5, 11, 9, 42, 3, 49]
mis_numeros = [3, 7, 11, 42, 34, 49]
numeros_ganadores = [3, 7, 11, 42, 34, 49]
hits = 0 # cuantas veces "le pegamos" al correcto
for numero in numeros_ganadores:
    if numero in mis_numeros:
        hits += 1
if hits == len(numeros_ganadores):
    print("Acertaste todos los números!")
else:
    print("Acertaste ",hits," números")
