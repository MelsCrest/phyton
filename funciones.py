#FUNCIONES
#FUNCIONES SIN ARGUMENTOS
# def rocket_parts():
#    print("payload, propellant, structure")
# print(rocket_parts())

#EXIGENCIA DE UN ARGUMENTO
# def distance_from_earth(destination):
#     if destination == "Moon":
#         return "238,855"
#     else:
#         return "Unable to compute to that destination"
# print(distance_from_earth("Moon"))

#VARIOS ARGUMENTOS NECESARIOS
# def days_to_complete(distance, speed):
#     hours = distance/speed
#     return hours/24
# print(days_to_complete(1000,30))

#FUNCIONES COMO ARGUMENTOS
#Opción 1
# total_days = days_to_complete(238855, 75)
# round(total_days)

#Opción 2
#round(days_to_complete(238855, 75))

# *********************************** #
#EJERCICIO TRABAJAR CON ARGUMENTOS EN FUNCIONES
# Fuel report:
#     Main tank: 80
#     External tank: 70
#     Hydrogen tank: 75

# def generate_report(main_tank, external_tank, hydrogen_tank):
#     output = f"""Fuel Report:
#     Main tank: {main_tank}
#     External tank: {external_tank}
#     Hydrogen tank: {hydrogen_tank} 
#     """
#     print(output)

# generate_report(80, 70, 75)

# ************************************** #
#USO DE ARGUMENTOS DE PALABRA CLAVE
# from datetime import timedelta, datetime

# def arrival_time(hours=51):
#     now = datetime.now()
#     arrival = now + timedelta(hours=hours)
#     return arrival.strftime("Arrival: %A %H:%M")

# COMBINACIÓN DE ARGUMENTOS Y ARGUMENTOS DE PALABRA CLAVE
# from datetime import timedelta, datetime

# def arrival_time(destination, hours=51):
#     now = datetime.now()
#     arrival = now + timedelta(hours=hours)
#     return arrival.strftime(f"{destination} Arrival: %A %H:%M")

