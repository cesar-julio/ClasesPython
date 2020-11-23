nombre = "César"
apellido = "López"
edad = 20
altura_en_cm = 170
ocupacion = "Mecánico"

#primera forma para imprimir varias variables
#str() "función que se usa para combertir enteros en cadenas"
print(nombre + " " + apellido + " tiene " + str(edad) + " años," + " mide " + str(altura_en_cm)+ " y trabaja de " + ocupacion)

#segunda forma para imprimir varias variables
print(nombre,apellido,"tiene",edad,"años,","mide",altura_en_cm,"y trabaja de",ocupacion)

#uso especifico de la función "str()"
text1 = "Cero es igual a "
text2 = 0
print(text1 + str(text2))

#otra forma de combertir un entero en cadena
segundo_nombre = "Julio"
dia_cumpleaños = str(21)
print(segundo_nombre + " cuple el día " + dia_cumpleaños + " años")

#cadenas formateadas
familia = "López"
integrante1 = "Malena"
integrante2 = "Lesli"
integrante3 = "Edinson"
edad_integrante3 = 42

print(f"La familia de los {familia} esta compuesta por {integrante1}, {integrante2} y {integrante3} el mayor que es papá tiene {edad_integrante3} años")




