from almacenes.Libreria import Libreria
from gui.Listados import Listados
from gui.Menus import Menus
from gui.Separadores import Separadores
class App:
    libreria = Libreria()
    @staticmethod
    def main():
        App.libreria.cargar_usuarios()
        App.libreria.cargar_editores()
        App.libreria.cargar_libros()
        App._gestionar_principal()

    @staticmethod
    def _gestionar_principal():
        fin = False
        while not fin:
            Menus.imprimir_menu_principal()
            entrada = input("¿Opción?>")
            match entrada.upper():
                case Menus.MENU_PRINCIPAL.SALIR.value:
                    break
                case Menus.MENU_PRINCIPAL.VER_LIBROS.value:
                    Listados.imprimir_almacen(App.libreria.libros)
                case Menus.MENU_PRINCIPAL.VER_USUARIOS.value:
                    Listados.imprimir_almacen(App.libreria.usuarios)
                case Menus.MENU_PRINCIPAL.VER_EDITORES.value:
                    Listados.imprimir_almacen(App.libreria.editores)
                case Menus.MENU_PRINCIPAL.PRESTAMOS.value:
                    App._gestionar_prestamos()

    @staticmethod
    def _gestionar_prestamos():
        fin = False
        while not fin:
            Menus.imprimir_menu_prestamos()
            entrada = input("¿Opción?>")
            match entrada.upper():
                case Menus.MENU_PRESTAMOS.SALIR.value:
                    break
                case Menus.MENU_PRESTAMOS.VER_PRESTAMOS.value:
                    Listados.imprimir_almacen_prestramos(App.libreria.prestamos)
                case Menus.MENU_PRESTAMOS.PRESTAR.value:
                    App._gestionar_prestar()
                case Menus.MENU_PRESTAMOS.DEVOLVER.value:
                    App._gestionar_devolver()

    @staticmethod
    def _gestionar_prestar():
        Listados.imprimir_almacen(App.libreria.libros)
        libro = int(input("Libro?"))
        Listados.imprimir_almacen(App.libreria.usuarios)
        usuario = int(input("Usuario?"))
        if App.libreria.hacer_prestamo(libro, usuario):
            Separadores.imprinmir_texto("Reserva Realizada")
        else:
            Separadores.imprinmir_error("Reserva No Realizada")

    @staticmethod
    def _gestionar_devolver():
        Listados.imprimir_almacen_prestramos(App.libreria.prestamos)
        prestamo = int(input("Prestamo?"))
        if App.libreria.devolover_libro(prestamo):
            Separadores.imprinmir_texto("Préstamo Devuelto")
        else:
            Separadores.imprinmir_error("Error al devolver")



App.main()
