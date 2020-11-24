contraseña = input("Crear contraseña: ")
print("Bienvenido al portal")
verificar_contraseña = input("Por favor, introduzca su contraseña: ")
#verifica la contraseña
if verificar_contraseña == contraseña:
    #imprime en pantalla el mensaje de bienvenida
    print("Acceso permitido !Bienvenido")
    #variable que contiene las posibilidades del usuario (int.- convierte a enteros)
    numeros = int(input("Escoja entre 1-3: "))
    if numeros == 1:
        numeros2 = input("Elige una letra M,F: ")
        if numeros2 == "M":
            print("Mejoras con el tiempo en tu trabajo")
        elif numeros2 == "F":
            print("Fundamenetas todas tus deciones fasilmente")
        else:
            print("Sabes que olvídalo")
    elif numeros == 2:
        print("Te gustan los gatos")
    elif numeros == 3:
        print("Eres una persona muy alegre")
    else:
        print("¿En serio? No puedes seguir instrucciones simples")
else:
    print("Contraseña equivocada")
#float.- combierte a números decimales
calificacion = float(input("Califique su experiencia del 1-3 puede usar decimales: "))

if calificacion >= 1.5:
    print("Gracias por considerar el esfuerso realizado")
elif calificacion <= 1.4:
    print("Diganos en que se puede mejorar:")
    input("Su recomendacion: ")
else:
    print("Intentelo usando los rangos sugeridos!!")
