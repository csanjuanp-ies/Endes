from dataclass.Editor import Editor
from almacenes.Almacen import Almacen
class Editores(Almacen):
    def __init__(self):
        super().__init__("Editores")

    def __str__(self):
        texto = ""
        for editor in self._objetos:
            texto += f"\t[{str(editor)}],\n"
        return f"[\n{texto}]"
