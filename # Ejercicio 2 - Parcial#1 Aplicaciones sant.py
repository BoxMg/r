# Ejercicio 2 - Parcial#1 Aplicaciones Web II
# Nombre:[Santiago rodriguez royero]

def calcular_impuesto(valor, impuesto=19):
    return valor + (valor * impuesto / 100)

total = 0
for i in range(3):
    precio = float(input("Ingrese el precio del producto: "))
    total += calcular_impuesto(precio)

print("El total con impuesto es:", total)
