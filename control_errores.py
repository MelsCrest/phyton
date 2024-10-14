# @ CONTROL DE ERRORES
# def main():
#     open("/path/to/mars.jpg") #Poner aquí el punto de ruptura

# if __name__ == '__main__':
#     main()

# @ CONTROL DE EXCEPCIONES
# try:
#      open('config.txt')
# except FileNotFoundError:
#      print("Couldn't find the config.txt file!")

#Opción 2 - Revisar
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")

#Opción 3 - Finally
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")
#     finally: 
#         print("Ok")

#Opción 4 - Revisar
# try:
#     open("config.txt")
# except OSError as err:
#      if err.errno == 2:
#          print("Couldn't find the config.txt file!")
#      elif err.errno == 13:
#         print("Found config.txt but couldn't read it")

# ********************************* #
# EJERCICIO CONTROL DE EXCEPCIONES

# loaded_config = """# Rocket Ship Configuration File!
# fuel_tanks=4
# oxygen_tanks=3
# initial_propulsion_level=84
# $ End of file"""

# parsed_config = {}
# for line in loaded_config.split('\n'):
#     try:
#         key, value = line.split('=')
#         parsed_config[key] = value
#     except ValueError:
#         print(f'Unable to parse {line}')
# print(parsed_config)

# ********************************* #

# @ GENERACIÓN DE EXCEPCIONES
# def water_left(astronauts, water_left, days_left):
#     for argument in [astronauts, water_left, days_left]:
#         try:
#             # If argument is an int, the following operation will work
#             argument / 10
#         except TypeError:
#             # TypeError will be raised only if it isn't the right type 
#             # Raise the same exception but with a better error message
#             raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
#     daily_usage = astronauts * 11
#     total_usage = daily_usage * days_left
#     total_water_left = water_left - total_usage
#     if total_water_left < 0:
#         raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
#     return f"Total water left after {days_left} days is: {total_water_left} liters"

#print(water_left("3", "200", None))

# ********************************* #
# EJERCICIO CONTROL DE EXCEPCIONES 2

# Imagine you are creating a program which will prompt the user for yes or no, which will be converted true or false. Because people will enter different values, you need to ensure the different possibilities are handled correctly. If an unknown response is given, the program should raise an error. For purposes of this exercise, you'll use the values below for true and false. Run the cell to load the variables.
# You will use true_values and false_values to create a function named str_to_bool to convert strings to Boolean values. str_to_bool will accept one parameter named value.
# Create the function str_to_bool. Convert value to lower case letters. If value matches an entry in true_values the function should return True. If value matches an entry in false_values it should return False. If it doesn't match any of the values, it should raise a ValueError, with a message of Invalid entry.

true_values = ['yes', 'y']
false_values = ['no', 'n']

def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError('Invalid entry')

try: 
    print(str_to_bool('1'))
except Exception as ex:
    print(ex)
#también se puede imprimir directamente sin hacer el try-except
#Haciendo print imprime toda la traza al dar error. Con try-except solo imprime la excepción