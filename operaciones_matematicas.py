#OPERACIONES MATEMÁTICAS
#El primer paso consiste en determinar el número de minutos que hay en 1042 segundos. Con 60 segundos en un minuto, puede dividir por 60 y obtener una respuesta de 17.3666667. El número que le interesa simplemente es 17. Se recomienda redondear hacia abajo, usando lo que se conoce como división de múltiplo inferior. Para realizar una división de este tipo en Python, debe utilizar '//'.
# seconds = 1042
# display_minutes = 1042 // 60
# print(display_minutes)

#Observe que se evalúan los paréntesis antes que cualquier otra operación. Usar paréntesis le permite asegurarse de que el código se ejecute de una manera predecible y el código resulta más fácil de leer y mantener. Como resultado, el procedimiento recomendado es usar paréntesis aunque el orden de las operaciones se evalúe de la misma manera sin ellos. En las dos líneas de código siguientes, la segunda es más comprensible porque el paréntesis indica claramente qué operación se realizará primero.
# result_1 = 1032 + 26 * 2
# print(result_1)

# result_2 = 1032 + (26 * 2)
# print(result_2)

#******************************************#

#EJERCICIO OPERACIONES ARITMÉTICAS 
#You have two variables which store the distance between each planet and a common point: the sun. You can subtract these two values to determine the distance between the planets. Start by adding the code to subtract first_planet from second_planet and store the result in a variable named distance_km. Display the value to the screen. Then add the code to convert distance_km to miles by dividing it by 1.609344 (the rough difference between miles and kilometers) and store the result in a variable named distance_mi. Display the value to the screen.

# first_planet = 149597870
# second_planet = 778547200
# distance_km = second_planet - first_planet  
# print(distance_km)
# distance_mi = distance_km / 1.609344
# print(distance_mi)

#*****************************************#

# @ int() y float() - Conversión de cadenas en números enteros y de punto flotante# 
# demo_int = int('215')
# print(demo_int)

# demo_float = float('215.3')
# print(demo_float)

# @ ABS() - Para valores absolutos 
# print(abs(39 - 16))
# print(abs(16 - 39))

# @ round() - Redondea hacia arriba al entero más cercano si es mayor de .5, y hacia abajo si es menor que .5.
# print(round(1.4))
# print(round(1.5))
# print(round(2.5))
# print(round(2.6))

# @ Python tiene bibliotecas para proporcionar operaciones y cálculos más avanzados:
# import math - importa todas las operaciones y calculos matematicos.
# from math import ceil, floor - importa especificamente esos dos métodos.

# from math import ceil, floor 
# @ ceil() - Redondea hacia arriba
# round_up = ceil(12.5)
# print(round_up)

# @ down() - Redondea hacia abajo
# round_down = floor(12.5)
# print(round_down)

# **************************************** #

#EJERCICIO APLICACION PARA TRABAJAR CON NUMEROS Y ENTRADA POR TECLADO
#To create our application, we want to read the distance from the sun for two planets, and then display the distance between the planets. We'll do this by using input to read the values, int to convert to integer, and then abs to convert the result into its absolute value. Start by adding the code to prompt the user for the distance between the sun and the first planet, and then the second. Store each result in variables named first_planet_input and second_planet_input.

first_planet_input = input("Enter the distance from the sun the first planet in km: ")
second_planet_input = input("Enter the distance from the sun the second planet in km: ")

#Because input returns string values, we need to convert them to numbers. Add the code to convert each input into an integer using int. Store the values in first_planet and second_planet respectively.

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

#With your values stored as numbers, you can now add the code to perform the calculation, subtracting the first planet from the second. Because the second planet might be a greater number, you'll use abs to convert it to an absolute value. Subtract first_planet from second_planet and convert the result to its absolute value by using abs. Store the result in a variable named distance_km. Then display the result on the screen.

distance_km = second_planet - first_planet
print(abs(distance_km))



