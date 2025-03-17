
    
estado_civil = input("soltero/casado/comprometido: ")
edad = int(input("Ingrese su edad: "))
temperamento = input("malgenido/a contento/a serio/a: ")
fisico = input("lindo/a feo/a: ")
salario = int(input("Ingrese su salario: "))
if estado_civil == "casado" or estado_civil == "comprometido":
    print("No puedes acercarte a  esa persona, por que ya esta comprometida")
elif edad < 18:                                                                                        
    print("No puedes acercarte a  esa persona, por que no tiene la edad suficiente")
elif temperamento == "mala persona":
      print("No puedes acercarte a  esa persona, por que te generari estres")
elif  fisico == "feo":
      print("No puedes acercarte a esa persona, por que no te atrae fisicamente")
elif salario < 2000000:
      print("No puedes acercarte a esa persona, por que gana mas dinero que tu")
else:
    print("Puedes acercarte a esa persona")
print("Fin del programa")



