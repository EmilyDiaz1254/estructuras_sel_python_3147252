'''
actividad3:
Escribir un programa 
que calcule el salario neto
de un trabajador
despuews de descuentos
y bonificaciones

=> INICIALMENTE, el diagrama 
trabajar entre los siguientes: 
a - contrato a termino indefenido
b - contrato por prestacion de servicios
c - contrato de aprendizaje 
d - jornal
=> jornal
   Se debe solicitar
   - Tipo de unidad a pagar
   - El numero de unidades hechas 
   - Valor de la unidad
   Descuentos de ley
   - 8% de salud
   - 10% de pension
   - 1% de caja de compensacion
   => contrato a termino indefinido 
   el salario es el que se calcula
   con base a la siguiente tabla:
   - 1: 1.5 veces el SMLV
    - 2: 2 veces el SMLV
    - 3: 2 veces el SMLV
    - 4: 2.5 veces el SMLV
    - 5: 3 veces el SMLV
    el programa debe solicitar
    el escalafon o grado
    del empleado

'''
#variable global:
#variable que puede ser reconocida
#Y asignada a cualquier parte del
#programa
#NOTA : se recomienda inicializar
#definir y dar valor inicial a las 
#variables globales al principio
#del programa
#ejemplo de esto son las variables
#para almacenar resultados finales


salario_neto = 0
tipo_empleado = input("Ingrese el tipo de empleado (a/b/c/d): ")

if tipo_empleado == "a":
    print("Ha ingresado contrato a término indefinido")
    SMLV = int(input("Ingrese el SMLV"))
    escalafon = int(input("Ingrese el escalafón:"))
    antiguedad = int(input("Ingrese la antigüedad en la empresa: "))
    if escalafon  == 1:
        salario_mensual = SMLV * 1.5
    elif escalafon == 2:
        salario_mensual = SMLV * 1.7
    elif escalafon == 3:
        salario_mensual = SMLV * 2.0
    elif escalafon == 4:
        salario_mensual = SMLV * 2.5
    elif escalafon == 5:
        salario_mensual = SMLV * 3.0
        
    # Bonificaciones : elif anidados
    bonificacion = 0
    if antiguedad < 2:
        bonificacion = salario_mensual * 0.02
    elif antiguedad >= 2 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.05
    elif antiguedad > 5:
        bonificacion = salario_mensual * 0.10
    salario_mensual += bonificacion
    # Descuentos
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.10
    descuento_caja = salario_mensual * 0.01
    salario_neto = salario_mensual - descuento_salud - descuento_pension - descuento_caja + bonificacion

elif tipo_empleado == "b":
    print("Ha ingresado contrato por prestación de servicios")
    valor_contrato = int(input("Ingrese el valor del contrato: "))
    numero_meses = int(input("Ingrese el número de meses trabajados: "))
    antiguedad = int(input("Ingrese la antigüedad en la empresa: "))
    salario_mensual = valor_contrato / numero_meses
    # Bonificaciones : elif anidados
    bonificacion = 0
    if antiguedad < 2:
        bonificacion = salario_mensual * 0.02
    elif antiguedad >= 2 and antiguedad <= 5:
        bonificacion = salario_mensual * 0.05
    elif antiguedad > 5:
        bonificacion = salario_mensual * 0.10
    salario_mensual += bonificacion
    # Descuentos
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.10
    descuento_caja = salario_mensual * 0.01
    salario_neto = salario_mensual - descuento_salud - descuento_pension - descuento_caja + bonificacion

elif tipo_empleado == "c":
    print("Ha ingresado contrato de aprendizaje")
    salario_minimo = int(input("Ingrese el salario mínimo: "))
    descuento = salario_minimo * 0.25
    salario_neto = salario_minimo - descuento

elif tipo_empleado == "d":
    print("Ha ingresado contrato de jornal")
    tipo_unidad = input("Ingrese el tipo de unidades (por ejemplo: horas, piezas): ")
    numero_unidades = int(input(f"Ingrese el número de {tipo_unidad} hechas: "))
    valor_unidad = int(input(f"Ingrese el valor de cada {tipo_unidad}: "))
    
    salario_neto = numero_unidades * valor_unidad
    
else:
    print("Tipo de empleado no válido")

print("El salario neto es:", salario_neto)
print("Fin del programa")
