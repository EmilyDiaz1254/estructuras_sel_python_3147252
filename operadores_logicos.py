'''

Operadores python

Aquellos que operan unicamente 
con valores booleanos(V F)
Acorde a las tablas de verdad
'''
#Ejemplo 1: Operador not:
y = not False

print("el resultado de operar con not es" ,y)

#Ejemplo 2: Operador and
y = False and True
print("El resultado de operar con and es" ,y)

#Ejemplo 3: Operador or
y=False or False
print("el resultado de operar con or es" ,y)


'''
Jerarquia de predencia de operadores
(logicoa inclusive)
1.  ()
2.  **
3.  *,/,%
4.  +,-
5.  >,<,>=,<=,!=,==
6.  not
7.  and
8.  or
'''

#Ejemplo 4:Jerarquia de operadores 
y = False and not True or False
print("el resultado de operar con jerarquia de operadores es", y)



#Ejemplo 5: operadores relacionales y logicos
y = not 3 > 4 and 4 -- 4 or 3<2
print("el resultado de operar con jerarquia de o", y)


#ejemplo 6: operadores aritmeticos
#realacionales y logicos

y = 3 + 5 * 2 > 10 and 4 == 4 or 3 < 20


# Ejemplo 7: con parentesis

y = ( 3 + 5 ) * ( 2 > 3 ) and 4 == 4  or not 3 < 2
