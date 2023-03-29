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
print(lst)
#   NameError: name lst is not defined












