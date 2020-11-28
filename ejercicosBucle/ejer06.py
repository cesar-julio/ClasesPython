# Escribir un programa que pida al usuario un
# número entero y muestre por pantalla un triángulo
# rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****
num = int(input("Número entero: "))
#Primera solución
for i in range(num+1):
    print("*" * i)

#Segunda solicón
for id in range(num):
    print("*" * (id+1))

#Tersera Soloción
for k in range(num):
    for h in range(k+1):
        print("*", end="")
    print("")


