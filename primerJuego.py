numero_secreto = 23
intentos_usuario = 0
max_intentos = 3
#inetentos
list_intentos = ["primer", "segundo", "terser"]

print("====== ADIVINA ADIVINADOR ======")
print("")
print("REGLAS\n *Tienes tres intentos para adivinar en número.")
print("")

while intentos_usuario < max_intentos:
    numero_usuario = int(input(f"Introdusca su {list_intentos[intentos_usuario]} intento: "))
    if numero_usuario == numero_secreto:
        print("================================")
        print("FELICIDADES ADIVINASTE EL NÚMERO")
        print("================================")
        break
    elif intentos_usuario < max_intentos - 1:
        print(">>>Estas serca vamos tu puedes!!")

    intentos_usuario += 1
else:
    print("")
    print("=====================")
    print("Perdiste el juego!!!")
    print("=====================")

