# Ejercicio 4 - Parcial#1 Aplicaciones Web II
# Nombre:[Santiago rodriguez royero]

try:
    saldo = int(input("Ingrese su saldo inicial: "))
    retiro = int(input("Ingrese el monto a retirar: "))

    if retiro > saldo:
        print("Error: Fondos insuficientes")
    elif retiro < 0:
        print("Error: No se permiten valores negativos")
    else:
        saldo -= retiro
        print("Retiro exitoso. Su saldo restante es:", saldo)

except ValueError:
    print("Error: Debe ingresar un número válido")
