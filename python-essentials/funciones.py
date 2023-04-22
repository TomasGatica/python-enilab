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
#
#   Cuando asignamos argumentos al parámetro correspondiente
#   le llamamos paso de parámetros posicionales.
def my_function_pos(a, b, c):
    print(a, b, c)
    print(c, b, a)
    #   los argumentos siguen el orden en que fueron
    #   definidos dentro de la función ()
my_function_pos(1,2,3)

#   Paso de argumentos de plabra clave
#   El significado del argumento está definido por su nombre
#   y no por su posición.
def nombre_apellido(nombre1, apellido1):
    print("Hola, mi nombre es: ", nombre1, apellido1)

nombre_apellido(nombre1="Tomás", apellido1="Gatica")
nombre_apellido(apellido1="Hernández", nombre1="Belén")
#   Observamos que la posición no es relevante
#   Si introducimos un nombre de parámetro que no existe
#   Python arrojará un TypeError got an unexpected 
#   keyword argument
#
#   Para mezclar args posicionales y de keywords
#   hay UNA SOLA REGLA INQUEBTRANTABLE:
#   Primero los args POSICIONALES y luego los KEYWORDS.
def func_suma(x,y,z):
    print("Sumamos ",x,y,z,"y su resultado es",x+y+z)

func_suma(1,2,3)
func_suma(z=3,y=2,x=1)
#   AHORA MEZCLAMOS
func_suma(3,z=1,y=2)
#   3 es pasado al pos x y los dos siguientes pueden 
#   ser puestos "desordenados", lo importante es respetar
#   el orden
#   func_suma(3,z=1,x=2)
#   $ TypeError multiple values for argument x 
#   OJO AL CASO DE KEY--POS = SyntaxError
#   POSITIONAL(orden) -- KEYWORD (desonrdando)
#
#   Ahora, podemos definir un parámetro con un argumento
#   default. Osea con un valor predefinido.
def nombre_apellido2(nombre1, apellido1="González"):
    print("Mi nombre es", nombre1, apellido1)

nombre_apellido2("Pedro", "Urdemales")
#   Si le pasamos un argumento se sobre escribe
nombre_apellido2("Jorge")
#   El apellido será el definido default de la func()
nombre_apellido2(nombre1="SlimShady")

def hi_my_name_is(nombre2="Slim", apellido2="Shady"):
    print("Hi my name is", nombre2, apellido2)

hi_my_name_is()
#   $ Hi my name is Slim Shady
print("Grande EMINEM")

#
def direccion(calle, ciudad, cod_postal):
    print("La dirección es calle", calle, "en la ciudad de", 
          ciudad, "con código postal", cod_postal)

street = input("Calle: ")
city = input("Ciudad: ")
postal_code = input("Código postal: ")

direccion(street,city,postal_code)

#   Si por algún motivo colocamos primero un arg KEYWORD
#   y luego uno POSICIONAL el error es de tipo SyntaxError

#   def sad(a,b=2,c):
#       print(a+b+c)
#   sad(a=1, c=3)
#   En este ejemplo estamos rompiendo la regla en la 
#   definción de la funcion el orden de los params pos-key