from almacenes.Almacen import Almacen
from dataclass.Libro import Libro
class Libros(Almacen):
    def __init__(self):
        super().__init__("Libros")

    def __str__(self):
        texto = ""
        for editor in self._objetos:
            texto += f"\t[{str(editor)}],\n"
        return f"[\n{texto}]"
