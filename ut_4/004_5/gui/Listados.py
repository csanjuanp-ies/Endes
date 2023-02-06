from gui.Separadores import Separadores
from almacenes.Almacen import Almacen
class Listados:
    ANCHO = Separadores.ANCHO
    @staticmethod
    def imprimir_almacen(almacen:Almacen):
        Separadores.imprimir_separador()
        print(almacen.titulo.center(Listados.ANCHO))
        for elemento in almacen:
            print(str(elemento))
            Separadores.imprimir_separador_secundario()
        Separadores.imprimir_separador()
