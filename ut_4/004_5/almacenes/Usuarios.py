from almacenes.Almacen import Almacen
from dataclass.Usuario import Usuario
class Usuarios(Almacen):
    def __init__(self):
        super().__init__("Usuarios")

    def __str__(self):
        texto = ""
        for usuario in self._objetos:
            texto += f"\t[{str(usuario)}],\n"
        return f"[\n{texto}]"
