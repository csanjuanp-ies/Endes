from almacenes.Libreria import Libreria
from gui.Listados import Listados
from gui.Menus import Menus
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
                    Listados.imprimir_almacen(App.libreria.prestamos)
                case Menus.MENU_PRESTAMOS.PRESTAR.value:
                    pass
                case Menus.MENU_PRESTAMOS.DEVOLVER.value:
                    pass


App.main()
