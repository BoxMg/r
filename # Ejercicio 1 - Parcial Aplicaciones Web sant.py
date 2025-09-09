# Ejercicio 1 - Parcial Aplicaciones Web II
# Nombre: [santiago rodriguez royero ]

numero = int(input("Ingrese un número entero positivo: "))

for i in range(1, numero + 1):
    print(f"\nTabla del {i}:")

    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
print(f"\nLa tabla más larga generada fue la del {numero}")
