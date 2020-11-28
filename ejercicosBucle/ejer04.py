# Escribir un programa que pida al usuario un número entero
# positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Escriva un número entero positivo: "))

#solo muestra los números naturales sin el cero
print("PRIMER CASO")
for i in range(numero):
    print(numero - i, end=",")

#nos muestra los números naturales incluyendo en cere
print("")
print("SEGUNDO CASO")
for e in range(numero,-1, -1):
    print(e, end=",")