#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
#y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad_invertir = float(input("Cuanto va a invertir: "))
interes_anual = float(input("Interes anual: "))
numero_años = int(input("Número de años: "))


for i in range(numero_años):
    cantidad_invertir *= 1 + interes_anual /100
    print(f"Capital tras {i +1} años: {round(cantidad_invertir, 2)}")#round es una función que redondea los números flotantes



