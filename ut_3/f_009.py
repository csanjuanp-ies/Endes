"""
Dados 10 números enteros introducidos por teclado, visualizar la suma de los pares,
cuántos páres existen y cuál es la media aritmética de los impares.
"""


def calcular(numeros):
    numero_actual = suma_pares = total_pares = total_impares = suma_impares = 0
    while numero_actual < len(numeros):
        numero = numeros[numero_actual]
        if numero % 2 == 0:  # par
            suma_pares += numero
            total_pares += 1
        else:
            suma_impares += numero
            total_impares += 1
        numero_actual += 1

    return suma_pares, total_pares, suma_impares, total_impares
