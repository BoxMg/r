# Ejercicio 3 - Parcial#1 Aplicaciones Web II
# Nombre:[Santiago rodriguez royero]

def analizar_numeros(*args, **kwargs):
    pares = []
    impares = []

    for n in args:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    if kwargs.get("mostrar_pares", False):
        print("Números pares:", pares, "(Total:", len(pares), ")")
    if kwargs.get("mostrar_impares", False):
        print("Números impares:", impares, "(Total:", len(impares), ")")

# Ejemplos de uso
analizar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, mostrar_pares=True)
analizar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, mostrar_impares=True)
