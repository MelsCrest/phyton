#LISTAS
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# @ Acceder a elementos de lista por índice:
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# print("The first planet is", planets[0])
# print("The second planet is", planets[1])
# print("The third planet is", planets[2])

# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# planets[3] = "Red Planet"
# print("Mars is also known as", planets[3])

# @ Determinación de la longitud de una lista:
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# number_of_planets = len(planets)
# print("There are", number_of_planets, "planets in the solar system.")

# @ Incorporación de valores a listas:
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# planets.append("Pluto")
# number_of_planets = len(planets)
# print("There are actually", number_of_planets, "planets in the solar system.")

# @ Eliminación de valores de listas:
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
# planets.pop()  # Goodbye, Pluto
# number_of_planets = len(planets)
# print("No, there are definitely", number_of_planets, "planets in the solar system.")

# @ Uso de índices negativos:
# print("The first planet is", planets[0])

# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# print("The last planet is", planets[-1])
# print("The penultimate planet is", planets[-2])

# @ Búsqueda de un valor en una lista:
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# jupiter_index = planets.index("Jupiter")
# print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# mercury_index = planets.index("Mercury")
# print("Mercury is the", mercury_index + 1, "planet from the sun")

# *************************************** #

#EJERCICIO LISTA DE PLANETAS
#First, create a variable named planets. Add the eight planets (without Pluto) to the list. The planets are: Mercury, Venus,Earth, Mars, Jupiter, Saturn, Uranus, Neptune. Finish by using print to display the list of planets.
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# print(planets)

#Next, display the total number of planets by using len and print.
# print(f"There are {len(planets)} planets.")

#Next, display the total number of planets by using len and print.
# planets.append("Pluto")
# print(f"Actually, there are {len(planets)} planets.")
# print(planets[-1], "is the last planet")

# *************************************** #

# @ Almacenamiento de números en listas:
# gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
# bus_weight = 124054 # in Newtons, on Earth

# print("On Earth, a double-decker bus weighs", bus_weight, "N")
# print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "N")

# @ Uso de min() y max() con listas:
# gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
# bus_weight = 124054 # in Newtons, on Earth

# print("On Earth, a double-decker bus weighs", bus_weight, "N")
# print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
# print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")
 
# MANIPULACIÓN DE DATOS DE LA LISTA
# @ Segmentación de listas:
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# planets_before_earth = planets[0:2]
# print(planets_before_earth)

# planets_after_earth = planets[3:8]
# print(planets_after_earth)

# planets_after_earth = planets[3:]
# print(planets_after_earth)

# @ Combinación de listas:
# amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
# galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

# regular_satellite_moons = amalthea_group + galilean_moons
# print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# @ Ordenación de listas:
# amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
# galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

# regular_satellite_moons = amalthea_group + galilean_moons
# regular_satellite_moons.sort()
# print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
# galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

# regular_satellite_moons = amalthea_group + galilean_moons
# regular_satellite_moons.sort(reverse=True)
# print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# **************************************** #

#EJERCICIO UTILIZAR TROZOS PARA RECUPERAR PARTES DE UNA LISTA

#First, create a variable named planets. Add the eight planets (without Pluto) to the list. The planets are: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#Next you will add the code to prompt the user for the name of a planet. You will do this by using input. Because strings are case sensitive in Python, ask the user to use a capital letter to start the name of the planet.
name_planet = input("Enter the name of the planet (with a capital letter to start)")

#Now it's time to determine which planets are closer than the one that the user entered. To do this, you need to find where he planet is in the list. You can use the index method to perform this operation. Add the code to find the index of the planet, and store it in a variable named planet_index.
planet_index = planets.index(name_planet)

#With the index determined, you can now add the code to display planets closer to the sun than the one selected. Use the slicing abilities of a list to display all planets up to the one selected.
print(f"Here are the planets closer than {name_planet}")
print(planets[0:planet_index])

#You can use the same index to display planets farther from the sun. However, remember that the starting index is included when you're using a slice. As a result, you'll have to add 1 to the value. Add the code to display the planets farther from the sun.
print(f"Here are the planets closer than {name_planet}")
print(planets[planet_index + 1:])

# **************************************** #