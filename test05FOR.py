#interamdo sobre una cadena
print("interamdo sobre una cadena")
for char in "loops":
    print(char)
print("")


print("interamdo sobre una lista")
for elm in ["Yo", "Amo", "Programar"]:
    print(elm)

print("")

print("Usando la función range")
for numero in range(15, 20):#el primer valor del parametro es el comienzo y el segundo el final
    print(numero)
print("Uso del range con un solo parámetro")
for num in range(10):
    print(num)
print("Uso del range con tres parámetros")
for nu in range(5, 20, 2):#el primer valor del parametro es el comienzo, el segundo el final y el tersero es periodo
    print(nu)
