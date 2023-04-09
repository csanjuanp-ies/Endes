from almacenes.Almacen import Almacen
from dataclass.Libro import Libro
class Libros(Almacen):
    def __init__(self):
        super().__init__("Libros")

    def __str__(self):
        texto = ""
        for libro in self._objetos:
            texto += f"\t[{str(libro)}],\n"
        return f"[\n{texto}]"
