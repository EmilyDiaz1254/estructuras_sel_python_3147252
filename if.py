'''

Estructura de control if:
Se utiliza para tomar desiciones 
basadas en expresiones condicionales
'''


#ejemplo 1: if SIMPLE
edad = int(input("Ingrese su edad: "))
documento = input ("Tienes documento? (si/no): ")
#condicional: si la edad es mayor o igual a 18
if edad >= 18 and documento=='si':
    #codigo para cuando es mayor a 18
    print("Eres mayor de edad y tienes documento, puedes votar")
else:
    #codigo para cuando es menor de 18
      print("Eres menor de edad o no tienes documento, no puedes votar")
#codigo que se ejecutga siempre
print("Fin del programa")


