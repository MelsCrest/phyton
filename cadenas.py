#CONCATENACIONES EN CADENAS

# fact = "The Moon has no atmosphere."
# two_facts = fact + "No sound can be heard on the Moon."
# print(two_facts)

# @ Para imprimir multilíneas usar triple comillas o '\n':
# multiline_n = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
# print(multiline_n)
# multiline = """Facts about the Moon:
#  There is no atmosphere. 
#  There is no sound."""
# print(multiline)

#MÉTODOS EN CADENAS
# @ .title() - La letra de cada palabra aparecerá en mayúscula:
# print("temperatures and facts about the moon".title()) 

# heading = "temperatures and facts about the moon"
# heading_upper = heading.title()
# print(heading_upper)

# @ .split() - Separa la cadena en cada espacio creando una lista con todas las palabras o números separados por un espacio:
# temperatures = "Daylight: 260 F Nighttime: -280 F"
# temperatures_list = temperatures.split()
# print(temperatures_list)

# @ \n - El carácter de nueva línea '\n' (implícito) se puede usar para dividir la cadena al final de cada línea, y crear líneas únicas:
# temperatures = "Daylight: 260 F\n Nighttime: -280 F"
# temperatures_list = temperatures.split('\n')
# print(temperatures_list)

# @ in - si existe una palabra, caracter o grupo de caracteres en una cadena. Es case sensitive, lo que busca ha de estar escrito de igual manera:
#print("Moon" in "This text will describe facts and challenges with space travel") #devuelve false, porque no hay 'Moon' en la frase
#print("Moon" in "This text will describe facts about the Moon") #devuelve true porque hay Moon en el texto

# @ .find() - Busca la posición de una palabra específica, si no la encuentra devuelve '-1':
#temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
#print(temperatures.find("Moon")) #-1

#temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
#print(temperatures.find("Mars"))  #64

# @ .count() - Devuelve el número total de repeticiones de una palabra determinada en una cadena:
#temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
#print(temperatures.count("Mars")) #1
#print(temperatures.count("Moon")) #0

# @ .lower() - Pasa la cadena de texto a minúsculas:
#print("The Moon And The Earth".lower())

# @ .upper() - Pasa la cadena de texto a mayúsculas:
#print("The Moon And The Earth".upper())

# @ [x] - Para imprimir uno de los elementos de la lista:
# temperatures = "Mars Average Temperature: -60 C"
# parts = temperatures.split(':')
# print(parts) #Se genera una lista con 2 elementos
# print(parts[-1]) #[-1] Devolvera el último elemento de la lista

# @ .isnumeric() .isdecimal() - Para devolver el elemento que sea un número al recorrer una lista. No se puede usar con números negativos '-70' ya que '-' es un caracter:
# mars_temperature = "The highest temperature on Mars is about 30 C"
# for item in mars_temperature.split():
#     if item.isnumeric(): #marca que el elemento a devolver al recorrer la lista sea numérico
#         print(item)

# @ .startswith() - Comprueba el primer carácter de una cadena:
#print("-60".startswith('E')) #true

# @ .endswith() - Comprueba el último carácter de una cadena:
#if "30 C".endswith("C"):
    # print("This temperature is in Celsius")

# @ .replace() - Para buscar y reemplazar repeticiones de un carácter o grupo de caracteres:
# print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

# @ .join() - Necesita un elemento iterable (como una lista de Python) como argumento, por lo que su uso es diferente al de otros métodos de cadena:
# moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
# print(' '.join(moon_facts)) #Se utiliza ' ' para unir todos los elementos de la lista.

#EJERCICIO TRANSFORMAR CADENA DE TEXTO
#text = "Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."

# Separar el párrafo en sentencias usando .split()
#sentences = text.split(". ")
#print(sentences)

# Encontrar palabras clave usando 'in'
#for sentence in sentences:
#    if "temperature" in sentence:
#       print(sentence)

#FORMATEO DE CADENAS DE TEXTO AL IMPRIMIR POR PANTALLA
#Formatear con el signo %s y %
# mass_percentage = "1/6"
# print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

#print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

#Con el método .format()
# mass_percentage = "1/6"
# print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

# mass_percentage = "1/6"
# print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

# mass_percentage = "1/6"
# print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

#Con f-strings
# mass_percentage = "1/6"
# print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

#Con f-springs no es necesario asignar un valor a una variable de antemano
# print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

#EJERCICIO FORMATEO DE STRINGS
# name = "Ganymede"
# planet = "Mars"
# gravity = '1.43'

# template = """Gravity Facts about {name}
# ----------------------------------
# Planet Name: {planet}
# Gravity on {name}: {gravity} m/s2"""
# print(template.format(name=name, planet=planet, gravity=gravity))

# template = f"""Gravity Facts about {name}
# {'-'*33}
# Planet Name: {planet}
# Gravity on {name}: {gravity} m/s2"""

# print(template)
