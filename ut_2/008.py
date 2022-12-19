"""
Crear el siguiente juego:

Su lógica es simple: dos o más jugadores recrean con la mano, sin mostrárselo a los demás,
la forma de una piedra (puño cerrado), un papel (mano abierta) o unas tijeras
(hacer una “V” con los dedos índice y corazón), y la tienen que sacar simultáneamente. La piedra gana a las tijeras
(las rompe), estas al papel (lo corta), y este a la piedra (lo envuelve).

El juego se desarrollará en tres pasos. Primero, habrá que definir las tres opciones. Luego, hay que darle al usuario
la posibilidad de elegir una, a la vez que el programa saca su opción aleatoriamente. Por último,
habrá que determinar quién ha ganado.

"""
import random

PAPEL = 0
TIJERAS = 1
PIEDRA = 2


def elegir_jugada_ordenador():
    return random.randint(PAPEL, PIEDRA)


def elegir_jugada_usuario():
    respuesta = -1
    while not PAPEL <= respuesta <= PIEDRA:
        respuesta = int(input("0.-Papel\n1.-Tijeras\n2.-Piedra\n¿Valor?"))
    return respuesta


def comprobar_ganador(ordenador, usuario):
    if ordenador == usuario:
        print(f"Empate ({ordenador=}-{usuario=})")
    elif (ordenador == TIJERAS and usuario == PAPEL) or \
            (ordenador == PIEDRA and usuario == TIJERAS) or \
            (ordenador == PAPEL and usuario == PIEDRA):
        print(f"Gana el ordenador ({ordenador=}-{usuario=})")
    else:
        print(f"Gana el usuario ({ordenador=}-{usuario=})")


def jugar():
    eleccion_ordenador = eleccion_jugador = False
    eleccion_ordenador = elegir_jugada_ordenador()
    eleccion_jugador = elegir_jugada_usuario()
    comprobar_ganador(eleccion_ordenador, eleccion_jugador)


jugar()
