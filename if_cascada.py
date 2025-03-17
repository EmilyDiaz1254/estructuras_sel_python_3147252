'''
if en cascada:
Estructura de control que permite 
evaluar varias condiciones en cascada, es decir, si la primera
condicion no se cumple,
se evalua la siguiente 
y asi sucesivamente.
'''

# Ejemplo 1: 
# Modificar el programa de votacion
# para que considere la edad de 17 
# Años

edad = int(input("Ingresa tu edad: ") )

if edad >= 18:
	print("Puedes votar.")
elif edad == 18:
	print("Bienevedido ciudanos, Puedes votar.")
elif edad == 17:
	print("Puedes votar hasta el proximo año.") 
elif edad >= 10:
    print("Eres muy pequeño, tienes registro civico.")  
elif edad < 17:
	print("No puedes votar aun .")     

print("Fin del programa") 