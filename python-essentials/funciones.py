#   Para qué nos sirven las funciones?
#   
#   - Cuando un fragmento de código se repite muchas veces
#   podemos considerar aislarlo en la forma de una func()
#   - Cuando el código comienza a crecer, con el fin de mejorar
#   la legibilidad. Esto se puede hacer mediante la descomposición
#   del problema. DIVIDE Y VENCERAS!
#   - Cuando ya descomponemos un problema el producto debiera ser 
#   implementado como un conjunto de funciones escritas por 
#   separado pero empacadas juntas en diferentes módulos.
#   En Python tenemos varios tipos de funciones:
#
#   Funciones Bult-in/Integradas, osea que son parte de Python.
#   Funciones que vienen de módulos presintalados en Python.
#   Definidas por el usuario directo en el código.
#   Lambdas func.
def mi_funcion():
    print("Cuerpo de la función")
#
#   Algunas reglas básicas: Las funciones no deben invocarse antes
#   de ser definidas. Las variables y funciones no deben tener el 
#   mismo nombre.
#   
#   Cuando se invoca una funcion, python recurda el lugar donde ocurre,
#   salta a la función invocada y al final vuelve al siguiente lugar
#   de donde fue invocada para continuar la ejecución.
#   
#   Exception NameError name 'mi_funcion' is not defined
#   La excepción que arrojará Python cuando la función es invocada
#   antes de ser definida.
#   
#   Si llegaramos definir una función y luego usar el mismo nombre
#   para una variable, Python olvida su rol anterior por lo que la
#   función ya no está disponible.
#
def hola():
    print("hola")
# hi(5)
#   Exception TypeError ya que hola no toma args
#
#   
#   Funciones PARAMETRIZADAS.

# def message(number):
#     print("mensaje", number)
# message()
#   Nos arrojará una excepción de TypeError ya que no encuentra el 
#   arg posicional. 
#
#   Los parámetros solo existen dentro de las funciones donde han sido 
#   definidos def func(param):
#   La asignación de un valor a un parámetro de una función se hace
#   en el momento que la func es llamada o invocada.
#   Por lo tanto, los argumentos existen fuera de las funciones, y 
#   son los que pasan los valores a los parámetros.
#
def mensaje(numero):
    print("Ingresa un número: ", numero)
mensaje(1)
# $ Ingresa un numero: 1
#  
#   Tambien es posible tener una variable con el mismo nombre de un parámetro.
numero = 123
mensaje(321)
print(numero)
# $ "Ingresa un numero: 321"
# $ 123
#   Como podemos observar la variable numero tiene un valor y el paramtro otro distinto
#   A esto se le denomina sombreado/shadowing
#
def funcion_param(que, algo):
    print("Ingresa", que, algo)
funcion_param("la cuenta", 1)
funcion_param("el rut", 891728)
funcion_param("la cosa", "rara")
#
#
#   El paso de paramtros sucede de dos maneras.
#   * Posicional (Positional)
#   * Palabra clave (Keywords)