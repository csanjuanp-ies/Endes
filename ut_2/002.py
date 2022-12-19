# import math
"""
Dados 10 números enteros introducidos por teclado, visualizar la suma de los pares,
cuántos páres existen y cuál es la media aritmética de los impares.
"""
# TOTAL_DE_NUMEROS = 10
# numero_actual = suma_pares = total_pares = total_impares = suma_impares = 0
# while numero_actual < TOTAL_DE_NUMEROS:
#     numero = int(input("¿Introduce el número " + str(numero_actual+1) + "?"))
#     if numero % 2 == 0:  # par
#         suma_pares += numero
#         total_pares += 1
#     else:
#         suma_impares += numero
#         total_impares += 1
#     numero_actual += 1
#
# print("La suma de los pares es:", suma_pares, "y el total es", total_pares)
# print("La media de los impares es", suma_impares / total_impares)

"""
El área A de un triángulo se puede calcular a partir del valor de dos de sus lados, a y b, y del ángulo que estos forman 
entre sí con la fórmula A = (a*b*sin(ang))/2. Diseña un programa que pida al usuario el valor de los dos lados 
(en metros), el ángulo que estos forman (en grados), y muestre el valor del área. 
(Ten en cuenta que la función sin de Python trabaja en radianes, así que el ángulo que leas en grados deberás 
pasarlo a radianes sabiendo que PI radianes son 180 grados. Prueba que has hecho bien el programa introduciendo l
os siguientes datos:a = 1, b = 2, angulo = 30; el resultado es 0.5.)
"""
# a = b = angulo = resultado = 0
# a = float(input("¿Lado a?"))
# b = float(input("¿Lado b?"))
# angulo = math.pi * int(input("¿Ángulo en grados?")) / 180
# resultado = a * b * math.sin(angulo) / 2
# print(resultado)
# print(round(resultado, 2))

"""
Aquí podemos ver el problema de trabajar con los números integrados
"""
# import numpy as np
# print(math.degrees(math.radians(30)))
# print(np.deg2rad(np.rad2deg(30)))
