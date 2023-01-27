import random

TAMANIO_POR_DEFECTO = 5
TAMANIO_MAXIMO = 10
FRECUENCIA = 0.1
DEPURAR = False
MINA = "M"
FALLO = "X"
VACIO = "-"
ACIERTO = "O"
MULTIPLICADOR_JUGADAS = 2


def juego():
    """
    Acción Juego
      establecer tablero
      Establecer minas
      Jugar
    Fin Juego
    """
    tablero = None
    tablero = establecer_tablero()
    numero_minas = establecer_minas(tablero)
    mostrar_tablero_dbg(tablero) if DEPURAR else None
    print(tablero) if DEPURAR else None
    jugar(tablero, numero_minas)


def establecer_tablero():
    """
    Accion establecer_tablero
        pedir numero de celdas
        si celdas mayor que máximo entonces celdas máximo
        crear tablero cuadrado
    Fin
    """
    tamanio = 0
    tablero = []

    tamanio = int(input("Número de celdas (máx 10?"))
    tamanio = tamanio if tamanio <= TAMANIO_MAXIMO else TAMANIO_POR_DEFECTO
    tablero = [[VACIO for _ in range(tamanio)] for _ in range(tamanio)]

    return tablero


def establecer_minas(tablero):
    """
    Accion establecer_minas
        determinar número minas a crear (10% total de huecos)
        mientras falten poner minas hacer
            elegir posición aleatoria
            si posición ya ocupada saltar
        fin mientras
        devolver numero_minas
    Fin

    """
    contador_minas = numero_minas = longitud = 0
    longitud = len(tablero[0])
    print(longitud) if DEPURAR else None
    numero_minas = round(longitud * longitud * FRECUENCIA)
    print(numero_minas) if DEPURAR else None
    while contador_minas < numero_minas:
        x = random.randrange(longitud)
        y = random.randrange(longitud)
        if tablero[x][y] == VACIO:
            tablero[x][y] = MINA
            contador_minas += 1

    return numero_minas


def jugar(tablero, numero_minas):
    """
    Accion jugar
        número jugadas El doble que minas
        mientras queden jugadas y no fin hacer:
            mostrar_tablero
            pedir posición
            acierto = hacer_jugada
            si no acierto entonces
                numero_jugadas -= 1
            sino
                fin = comprobar fin juego
        fin mientras
        sin fin entonces
            "has gando"
        sino
            "has perdido"
    Fin
    """
    fin = False
    numero_jugadas = numero_minas * MULTIPLICADOR_JUGADAS
    while numero_jugadas > 0 and not fin:
        mostrar_tablero(tablero)
        posicion_x = int(input("Posición x?"))
        posicion_y = int(input("Posición y?"))
        acierto = hacer_jugada(tablero, posicion_x, posicion_y)
        if not acierto:
            numero_jugadas -= 1
            print(numero_jugadas) if DEPURAR else None
        else:
            fin = comprobar_fin_juego(tablero)

    if fin:
        print("Has ganado")
    else:
        print("Has perdido")


def mostrar_tablero(tablero):
    """
    Accion mostrar_tablero
        mostrar cabecera
        para cada fila
            imprimir número fila
            para cada columna
                si no es la mina
                    imprimir elemento
                sino
                    imprimir vacio
    Fin

    """
    longitud_lado = len(tablero[0])
    print("  ", " ".join([str(x) for x in range(longitud_lado)]))
    for x in range(longitud_lado):
        print(x, " ", end='')
        for y in range(longitud_lado):
            if tablero[x][y] != MINA:
                print(tablero[x][y], "", end="")
            else:
                print(VACIO, "", end="")
        print("")


def hacer_jugada(tablero, x, y):
    """
    Accion hacer_jugada
        si jugada es Mina
            cambiar tablero a acierto
            devolver true
        sino
            cambiar tablero a fallo
            devolver falso
    Fin
    """
    resultado = False
    if tablero[x][y] == MINA:
        tablero[x][y] = ACIERTO
        resultado = True
    else:
        tablero[x][y] = FALLO

    return resultado


def comprobar_fin_juego(tablero):
    """
    Accion comprobar_fin_juego
        si no hay más minas
            devolver true
        sino
            devolver fallo
    Fin
    """
    return True if MINA not in [i for item in tablero for i in item] else False


def mostrar_tablero_dbg(tablero):
    """
    Muestra el tablero completo, sin ocultar las minas, para depuración

    :param tablero: tablero del juego.
    :return: None
    """
    longitud_lado = len(tablero[0])
    print("  ", " ".join([str(x) for x in range(longitud_lado)]))
    for x in range(longitud_lado):
        print(x, " ", end='')
        for y in range(longitud_lado):
            print(tablero[x][y], "", end="")
        print("")


juego()
