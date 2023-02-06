from datetime import datetime

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
        libro.disponible = False
        nuevo_prestamo = Prestamo(usuario.nombre)
        nuevo_prestamo.fecha_de_prestamo = datetime.now()
        nuevo_prestamo.libro = libro
        nuevo_prestamo.usuario = usuario
        self.append(nuevo_prestamo)

    def devolver_libro(self, prestamo:Prestamo):
        prestamo.cerrar_prestamo()
        if not prestamo.devuelto_correcto:
            return "Devuelto Tarde"

