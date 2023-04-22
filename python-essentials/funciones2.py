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