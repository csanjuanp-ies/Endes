num_filas = int(input("Número de filas (mínimo 1):"))
num_columnas = int(input("Número de columnas (mínimo 2):"))
num_filas = 1 if num_filas < 1 else num_filas
num_columnas = 2 if num_columnas < 2 else num_columnas
columna_actual = 1
fila_actual = 0

while fila_actual < num_filas:
    while columna_actual < num_columnas and fila_actual < num_filas:
        print(" " * (columna_actual-1) + "*")
        columna_actual += 1
        fila_actual += 1
    columna_actual = num_columnas
    while columna_actual > 1 and fila_actual < num_filas:
        print(" " * (columna_actual - 1) + "*")
        columna_actual -= 1
        fila_actual += 1
    columna_actual = 1
