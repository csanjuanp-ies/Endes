from almacenes.Almacen import Almacen
from dataclass.Prestamo import Prestamo
class Prestamos(Almacen):
    def __init__(self):
        super().__init__("Prestamos")

    def __str__(self):
        texto = ""
        for prestamo in self._objetos:
            texto += f"\t[{str(prestamo)}],\n"
        return f"[\n{texto}]"
