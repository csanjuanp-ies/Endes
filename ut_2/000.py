"""
num_1 = 0
num_2 = 0
resto = 0
Escribir "Introduce dos número"
Leer num_1, num_2
si num_1 < num_2 entonces
    aux = num_1
    num_1 = num_2
    num_2 = aux
FinSi
Mientras num_2 <> 0 hacer
    resto = num_1 mod num_2
    num_1 = num_2
    num_2 = resto
FinMientras
Imprimir num_1
"""
num_1 = 0
num_2 = 0
resto = 0
print("Introduce dos número")
num_1 = int(input("Num_1:"))
num_2 = int(input("Num_2:"))
if num_1 < num_2:
    aux = num_1
    num_1 = num_2
    num_2 = aux

while num_2 != 0:
    resto = num_1 % num_2
    num_1 = num_2
    num_2 = resto

print(num_1)
