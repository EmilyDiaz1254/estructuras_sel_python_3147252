'''
if anidados
son estructuras selectivas
que se encuentran dentro
de otro if
sintax:
if condicion:
    if condicion:
        if condicion:
            bloque de instr
    else:
        if condicion:
            bloque de instr
else:
    bloque de instrucciones
'''

#Ejemplo 1:
#modificacion de ejercicio de votacion
#ahora solo puede votar si es mayor de edad
#pero si tiene documento.
#mostrar explicaciones en los otros casos
edad =int (input("ingrese su edad: "))
if edad>=18:
    documento=input("Tiene documento? (si/no):")
    if documento== "si":
        print("Usted puede votar")
    else:
        print("Usted no puede votar")
        print("Porque no tiene documento")
else:
    print("Usted no puede votar")
    print("Porque es menor de edad")

      