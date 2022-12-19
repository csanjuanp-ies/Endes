# Definición de variables y constantes
ERROR = -1
POS_INICIAL = 0
encontrado = False
posicion = 0
# Petición al usuario de los datos
cadena = input("Introduce una cadena:")
subcadena = input("Introduce una subcadena:")

if 0 < len(subcadena) < len(cadena):  # Qué pasa si ponemos una subcadena vacía
    while not encontrado and posicion < len(cadena):  # Recorremos todos los caracteres uno a uno
        if cadena[posicion:posicion+len(subcadena)] == subcadena:  # Buscar coincidencias
            encontrado = True
        else:
            posicion += 1
    if encontrado:
        print(posicion)
    else:
        print(ERROR)
elif cadena == subcadena:  # len(subcadena) == len(cadena) --> NO es necesaario
    print(POS_INICIAL)
else:  # subcadena será mayor que cadena en este caso
    print(ERROR)

# Probar con las dos cadenas vacías
# Probar con la subcadena vacía
# Probar con una subcadena al principio, final, mnedio, de longitud uno, de longitud uno menos que la cadena al inicio
# y al final, de diversas longitudes
