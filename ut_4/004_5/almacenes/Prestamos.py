from almacenes.Almacen import Almacen
from dataclass.Libro import Libro
from dataclass.Prestamo import Prestamo
from dataclass.Usuario import Usuario


class Prestamos(Almacen):
    def __init__(self):
        super().__init__("Prestamos")

    def __str__(self):
        texto = ""
        for prestamo in self._objetos:
            texto += f"\t[{str(prestamo)}],\n"
        return f"[\n{texto}]"

    def realizar_prestamo(self, libro:Libro, usuario:Usuario):
        # Crear nuevo Prestamo
        # Establecer libro a no disponible
        # Configurar datos del préstamo
        # self.append(nuevo_prestamo)
        pass

    def devolver_libro(self, prestamo:Prestamo):
        # Establecer disponible el libro
        # Establecer fecha de devolución
        # Devolver error si devolución tarde
        pass

    def get_index_del_prestamo(self, prestamo: Prestamo):
        # buscar en todos los préstamos no cerrados
        # devolver el índice
        pass