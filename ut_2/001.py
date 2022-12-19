"""
#  Con Errores
edad = int(input("Introduce tu edad:"))
fin = False
while not fin:
    if edad > 18:   # error >=
        fecha_nacimiento = int(input("Introduce la fecha de nacimiento (YYYYMM):"))
        anio_actual = int(input("Introduce el año de cálculo (YYYY):"))
        anio_nacimiento = fecha_nacimiento // 10000   # error es 100
        meses = fecha_nacimiento % 100
        edad = anio_actual - anio_nacimiento  # error nombrarla así interfiere con la del if
        edad_calculada_meses = edad * 12 + meses
        if edad_calculada > 0:
            print("Tu edad es:", edad, "en años")
            print("Tu edad es:", edad_calculada_meses, "en meses")
        else:
            print("Datos erróneos")

        fin = input("Fin(Si)?") == 'si'   # error Debe ser Si, no entra si edad < 18
"""
"""
#  Sin errores

edad = int(input("Introduce tu edad:"))
fin = False
while not fin:
    if edad >= 18:
        fecha_nacimiento = int(input("Introduce la fecha de nacimiento (YYYYMM):"))
        anio_actual = int(input("Introduce el año de cálculo (YYYY):"))
        anio_nacimiento = fecha_nacimiento // 100
        meses = fecha_nacimiento % 100
        edad_calculada = anio_actual - anio_nacimiento
        edad_calculada_meses = edad_calculada * 12 + meses
        if edad_calculada > 0:
            print("Tu edad es:", edad_calculada, "en años")
            print("Tu edad es:", edad_calculada_meses, "en meses")
        else:
            print("Datos erróneos")

    fin = input("Fin(Si)?") == 'Si'
"""
