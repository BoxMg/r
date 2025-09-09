# Ejercicio 5 - Parcial#1 Aplicaciones Web II
# Nombre:[Santiago rodriguez royero]

productos = []

while True:
    nombre = input("Ingrese el nombre del producto (o 'fin' para salir): ")
    if nombre.lower() == "fin":
        break
    precio = float(input("Ingrese el precio: "))
    productos.append({"nombre": nombre, "precio": precio})

print("\n--- Reporte Final ---")
print("Total productos:", len(productos))

suma = 0
for p in productos:
    suma += p["precio"]
promedio = suma / len(productos)
print("Precio promedio:", promedio)

caro = productos[0]
barato = productos[0]
for p in productos:
    if p["precio"] > caro["precio"]:
        caro = p
    if p["precio"] < barato["precio"]:
        barato = p

print("Producto más caro:", caro)
print("Producto más barato:", barato)

ordenados = sorted(productos, key=lambda x: x["precio"], reverse=True)
print("\nProductos ordenados de mayor a menor precio:")
for p in ordenados:
    print(p)
