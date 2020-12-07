print("!Bienvenido al sentro de prestamos de tu banco CEPE!")
print("")
print("Complete el formulário")

edad = int(input("Cual es su edad: "))
trabajando = input("Esta trabajando [si/no]: ")
casado = input("Esta casado [si/no]: ")
tiene_antecedentes_penales = input("Tiene atecedentes penales [si/no]: ")
tiene_licencia = input("¿Tienes licencia? [si/no]: ")
salario_mensual = int(input("Su salario mensual [/S.]: "))

estados = [trabajando, casado, tiene_antecedentes_penales, tiene_licencia]
for i in range(3):
    if estados[i].lower() == "si":
        estados[i] = True
    else:
        estados[i] = False

if estados[2] != True:
    print("!Tiene derecho a un préstamo!")
else:
    print("Lo siento, pero no eres elegible para un préstamo.")

if edad <= 35:
    print("La edad esta bien.")
else:
    print("Estás por encima de nuestro límite de edad máximo.")

if salario_mensual >= 3500:
    print("Perfecto! Eres elegible.")
else:
    print("Lo siento, pero estás por debajo de nuestro requisito mínimo.")

if estados[3] != True:
    print("Tiene una licencia valida")
else:
    print("No tiene una licencia valida")


