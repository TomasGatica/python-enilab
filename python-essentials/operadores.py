#   El operador es un símbolo capaz de realizar
#   operaciones con los valores.
#   + suma - resta * multiplicación
#   / división // división entera
#   % resto ** exponenciación
#
#   Exponenciación
print(2 ** 3)
print(2. ** 3.)
print(2 ** 3.)
#   Con ambos valores como enteros resultado entero
#   con al menos 1 flotante, resultado flotante.
#   
#   Multiplicación
print(2 * 3)
print(2. * 3.)
print(2 * 3.)
#
#   División
print(2 / 3)
print(2. / 3.)
print(6 / 3.)
#   Notar que en la división, el resultado siempre es
#   flotante.
#   Para cuando necesitamos que sea entero usamos //
#   División entera
print(6 // 3)
print(2. // 3.)
print(6 // 3.)
#   Los resultados son redondeados, y en caso de haber
#   flotantes, el resultado es flotante.
#   la parte fraccionaria siempre es igual a 0
#   EL REDONDEO SIEMPRE VA HACIA ABAJO
#   en negativos:
print(-6 // 4)  #   $ -2
print(6. // -4) #   $ -2.0 
#   -1.5 es redondeado al valor más bajo, -2.
#
#   Módulo, resto o residuo de la división entera.
print(14 % 4)
#   14 // 4 = 3 luego 3 * 4 = 12 y 14 - 12 = 2 RESTO
print(12 % 4.5)
#   12 // 4.5 = 2.0 luego 2.0 * 4.5 = 9.0
#   y 12 - 9.0 = 3.0 Resto
#
#   Operadores unarios y binarios
#   Suma, resta, multiplicación y división.   
#
#   Resta: espera dos argumentos el IZQ minuendo
#   y el DER sustraendo.
print(+2)   #   $ 2.0 

#   Operadores y sus enlaces
#   Los operadores deben responder a una jerarquía
#   de prioridades para determinar el orden 
#   de ejecución en que se computan las operaciones.
#   En Python la mayoría son de enlazado hacia la izquierda.
#   Por lo que el cálculo se hace de IZQ A DER.
print(9 % 6% 2) #   $ 1
print(2 ** 2 ** 3)  #   $ 256
#   El operador de EXPONENCIACIÓN usa enlazado del lado derecho.
#
#   Prioridades:
#   1. ** 
#   2. + - unario
#   3. * / // % 
#   4. + - binario
print(2 * 3 % 5)    #   * y % tienen la misma prioridad
                    #   por lo que el resultado está determinado 
                    #   conociendo el sentido del enlazado
                    #   $ 1
#
#   Las sub-expresiones dentro de los paréntesis siempre se calculan primero
