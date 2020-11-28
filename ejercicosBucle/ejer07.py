# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
print("================= Tabla de multiplicar 01 ================")
for i in range(1,13):
    for k in range(1,13):
        print(i*k, end="\t") # \t = esto sirve para hacer una tabulación
    print("")
# Otra forma de presentar la tabla
print("")
print("================= Tabla de multiplicar 02 ================")
for i in range(1,13):
    for k in range(1,13):
        print(f"{i} * {k} = {i*k}")
    print("")