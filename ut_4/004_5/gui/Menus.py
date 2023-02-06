from enum import Enum
from gui.Separadores import Separadores


class Menus:
    ANCHO = Separadores.ANCHO
    class MENU_PRINCIPAL(Enum):
        VER_LIBROS = "1"
        VER_USUARIOS = "2"
        VER_EDITORES = "3"
        PRESTAMOS = "4"
        SALIR = "S"
    class MENU_PRESTAMOS(Enum):
        VER_PRESTAMOS = "1"
        DEVOLVER = "2"
        PRESTAR = "3"
        SALIR = "S"
    @staticmethod
    def imprimir_menu_principal():

        Menus._imprimir_cabecera()
        print("Menú principal".center(Menus.ANCHO))
        Separadores.imprimir_separador()
        print("1.- Ver libros")
        print("2.- Ver Usuarios")
        print("3.- Ver Editores")
        Separadores.imprimir_separador()
        print("4.- Prestamos/Devoluciones")
        Separadores.imprimir_separador()
        print("S.- Salir")
        Separadores.imprimir_separador()

    @staticmethod
    def _imprimir_cabecera():
        Separadores.imprimir_separador()
        print("(c) 2023".center(Menus.ANCHO))
        Separadores.imprimir_separador()


    @staticmethod
    def imprimir_menu_prestamos():
        Menus._imprimir_cabecera()
        print("Menú prestamos".center(Menus.ANCHO))
        Separadores.imprimir_separador()
        print("1.- Ver Prestamos")
        print("2.- Devolver")
        print("3.- Prestar")
        Separadores.imprimir_separador()
        print("S.- Salir (Volver principal)")
        Separadores.imprimir_separador()
