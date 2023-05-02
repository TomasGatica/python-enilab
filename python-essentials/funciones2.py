#   La instrucción return

def teemo(de_servicio=True):
    print("Dos")
    print("Tres")
    print("Cuatro")
    if not de_servicio:
        return
    print("Capitán Teemo de Servicio!")

teemo()
print("---------")
teemo(False)

def draven():
    print("adivina...")
    return "Draaaaaaaven"

mejor_pj_lol = draven()
print("El mejor pj en LoL es", mejor_pj_lol)

#   Ahora analicemos el caso donde perdemos el return
print("-----------")
def draven_draven():
    print("Adivina quien es el mejor pj en LoL")
    return "Draaaaaaaven"
draven_draven() #   Solo estamos invocando la funcion
#   Pero no almacenando su valor de retorno
#   Si una función intenta devolver un dato útil
#   debemos asignarla a una variable.
#
#
#   None Keyword 
#   Para representar nada xd, utilizamos None.
#   None en si tiene su propio tipo NoneType
#   Recordemos que no representa nada.
#   Si intentamos por ejemplo sumar un None + un int u otro
#   Python arrojará un TypeError, ya que el operando + 
#   no soporta la suma de un NoneType con un int
#
#   None nos puede servir de manera segura cuando 
#   la asignamos a una variable (o devuelta como resultado
#   de una función) o cuando lo comparamos con una var
#   para diagnosticar su estado interno.
value = None
if value is None:
    print("Lo sentimos, no hay ningún valor")
#   OBS: si una función no devuelve un valor utilizando
#   la expresión return se asume ÍMPLICITAMENTE
#   que devuelve en realidad un None.
#   Recuerda que el cuerpo de una función puede contener 
#   Instrucciones que se ejecutan pero no es lo mismo
#   a tener un valor de retorno.
def funcion_rara(num):
    if (num % 2 == 0):
        return True
print(funcion_rara(2)) # $ True
print(funcion_rara(1)) # $ None
#
#
#   Listas y funciones
#   Podemos enviar listas como argumentos, y en general, cualquier
#   entidad reconocible por Python puede tomar el papel 
#   de un arg de func. Pero hay que serciorarse de que la func
#   sea capaz de hacer uso de él.
def sumar_items_lista(lista):
    
    acumulador = 0
    
    for item in lista:
        acumulador += item
        
    return acumulador

print(sumar_items_lista([5, 4, 3]))
#   Una manera riesgosa a tener en cuenta es cuanto solo le pasamos
#   un argumento literal.
#   print(sumar_items_lista(5)) nos arrojará un TypeError
#   debido a que el objeto 'int' no es iterable.
#
#
#   También podemos devolver una lista como 
#   resultado de una función, al igual que otras entidades
#   válidas.

def agregar_num_lista(n):
    
    lista_numeros = []
    
    for i in range(0, n):
        lista_numeros.insert(0, i)
    
    return lista_numeros

print(agregar_num_lista(10))    # $ [9, 8, 7, ..., 0]

#
#
#   Lab: Cuantos días. Escribir una funcion que toma dos args
#   un año y mes, y devuelve el número de días del 
#   mes/año dado (mientras que solo febrero es sensible al 
#   valor del año).

def es_bisiesto(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
def dias_en_mes(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    respuesta = days[month - 1]
    if month == 2 and es_bisiesto(year):
        respuesta = 29
    return respuesta

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print("Year ", yr, "month ", mo, "-> ", end="")
    result = dias_en_mes(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
        
#   Encontrando números primos.
def es_primo(num1):
    for i in range(2, int(1 + num1 ** 0.5)):
        if num1 % i == 0:
            return False
    return True
    
for i in range(1, 20):
    if es_primo(i + 1):
        print(i + 1, end=" ")
print()