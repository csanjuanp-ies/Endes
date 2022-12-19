ultima = int(input("Última a mostrar:"))
saltar = int(input("Tabla a saltar:"))
for a in range(1, 11):
    if a == ultima:
        break
    if a == saltar:
        continue
    for b in range(1, 11):
        print(f"{a}x{b}={a*b}")
