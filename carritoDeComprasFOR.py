carrito_compras = [1, 4, 5, 7, 9]
objetos_comprados = ["Lamina", "Helado", "Calsón", "Malena","Cuaderno"]
total = 0
indice = 0

for i in carrito_compras:
    print(f"{objetos_comprados[indice]} ------- S/.{i}")
    indice += 1
    total += i


print(f"El precio total es de: S/. {total}")