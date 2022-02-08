## Variables

# # 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
variable_int = 3

# 2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(variable_int))

# 4) Crear una variable que contenga tu nombre
mi_nombre = 'Adrian'

# 5) Crear una variable que contenga un número complejo
variable_compleja = 1 + 2j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(variable_compleja))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
variable_pi = 3.1415

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable_bool = True
variable_str = 'True'
# No son lo mismo, una es bool y la otra string

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(variable_bool))
print(type(variable_str))

# 10) Asignar a una variable, la suma de un número entero y otro decimal
variable_10 = 1 + 0.5

# 11) Realizar una operación de suma de números complejos
(1 + 2j) + (3 + 5j)

# 12) Realizar una operación de suma de un número real y otro complejo
1 + (2 + 0.5j)

# 13) Realizar una operación de multiplicación
3 * 2

# 14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27 / 4
print(cociente)

# 16) De la división anterior solamente mostrar la parte entera
parte_entera = 27 // 4
print(parte_entera)

# 17) De la división de 27 entre 4 mostrar solamente el resto
resto = 27 % 4
print(resto)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(parte_entera * 4 + resto)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
str1 = 'Hola '
str2 = 'mundo'
print(str1 + str2)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2" == 2)
# Son distintos tipos

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print("2" == str(2))

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# Porque la coma decimal se representa con un punto.

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
variable23 = 10
variable23 -= 7
print(variable23)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<2)

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# No se puede realizar directo, es necesario hacer un casting previamente. El resultado siempre seria el mismo si ambos son del mismo tipo.

# 26) Realizar una operación válida entre valores de tipo entero y string
print(2 + int('2'))
