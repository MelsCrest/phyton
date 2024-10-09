# IMPORTAR LIBRERIAS DE PYTHON
# FECHAS
#from datetime import date

#print(date.today())
#print("Today's date is: " + date.today()) #Da error porque no entiende el date como string
#print("Today's date is: " + str(date.today())) #Cambiar el tipo a 'string'

# EJERCICIO AÑOS LUZ
#parsecs = 11
#lightyears = parsecs * 3.26

#print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears") #Texto sin formatear

#print(f"{parsecs} parsecs is {lightyears} lightyears") #Texto formateado. Se pone una 'f' al principio y las variables, sin forzar su tipo, entre llaves

#RECUPERAR ARGUMENTOS DE LA LÍNEA DE COMANDOS
#import sys

#Escribir en el Terminal py nombredelprograma.py lo que sea
#Ej: py librerias.py hola
#Y ya lo ejecutamos
#print(sys.argv)
#print(sys.argv[0]) # program name
#print(sys.argv[1]) # first arg

parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(f"{parsecs_input} parsecs is {lightyears} lightyears")

