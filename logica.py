# CONDICIONAL IF sin parentesis ni llaves
# a = 93
# b = 27
# if a >= b:
#     print(a)

# a = 24
# b = 44
# if a <= 0:
#     print(a)
# print(b)

# IF Y ELSE
# a = 27
# b = 93
# if a >= b:
#     print(a)
# else:
#     print(b)

#ELSE IF
# a = 27
# b = 93
# if a <= b:
#     print("a is less than or equal to b")
# elif a == b:
#     print("a is equal to b")

# IF, ELSE IF, ELSE
# a = 27
# b = 93
# if a < b:
#     print("a is less than b")
# elif a > b:
#     print("a is greater than b")
# else: 
#     print ("a is equal to b")

#EJERCICIO TAMAÑO ESCOMBROS ESPACIALES
# You will start your project by creating the code to determine if a piece of space debris is of a dangerous size. For this exercise we will use an arbitrary size of 5 meters cubed (5m3); anything larger is a potentially dangerous object. For this step you will be presented with the goal for the exercise, followed by an empty cell. Enter your Python into the cell and run it. The solution is at the bottom of the exercise. In the cell below, add a variable named object_size and set it to 10 to represent 10m3. Then add an if statement to test if object_size is greater than 5. If it is, display a message saying We need to keep an eye on this object. Otherwise, display a message saying Object poses no threat.

#object_size = 3
# if object_size > 5:
#     print("We need to keep an eye on this object.")
# else: 
#     print("Object poses no threat")

#OPERADOR TERNARIO
#("We need to keep an eye on it" if object_size > 5 else "Object poses no threat")

#OPERADORES TERNARIOS 'and' Y 'or'
#OPERADOR 'or'
# a = 23
# b = 34
# if a == 34 or b == 34:
#     print(a + b)

#OPERADOR 'and'
# a = 23
# b = 34
# if a == 23 and b == 34:
#     print (a + b)

#EJERCICIO MANIOBRA EVASIVA
#In the previous exercise you created code to test the size of the object. Now you will test both the object's size and proximity. You will use the same threshold for size of 5m3. If the object is both larger than the threshold and within 1000km of the ship evasive maneuvers will be required. For this step you will be presented with the goal for the exercise, followed by an empty cell. Enter your Python into the cell and run it. The solution is at the bottom of the exercise. Add the code to the cell below to create two variables: object_size and proximity. Set object_size to 10 to represent 10m3. Set proximity to 9000. Then add the code to display a message saying Evasive maneuvers required if both object_size is greater than 5 and proximity is less than 1000. Otherwise display a message saying Object poses no threat.

object_size = 10
proximity = 9000

# if object_size > 5 and proximity < 1000:
#     print("Evasive maneuvers required")
# else:
#     print("Object poses no threat")

# OPERADOR TERNARIO
print("Evasive maneuvres required" if object_size > 5 and proximity < 1000 else "Object poses no threat")
