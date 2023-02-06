from dataclass.Libro import Libro
from dataclass.Usuario import Usuario
import datetime
class Prestamo:
    DIAS_DE_PRESTAMO_POR_DEFECTO = datetime.timedelta(days=5)
    def __init__(self, asunto):
        self._libro = None
        self._usuario = None
        self.asunto = asunto
        self.fecha_de_prestamo = datetime.datetime.now()
        self.fecha_de_devolucion = self.fecha_de_prestamo + Prestamo.DIAS_DE_PRESTAMO_POR_DEFECTO

    def __eq__(self, other:"Prestamo"):
        return self._libro == other._libro and \
            self._usuario == other._usuario and \
            self.fecha_de_prestamo == other.fecha_de_prestamo
    @property
    def libro(self):
        return self._libro

    @libro.setter
    def libro(self, valor: Libro):
        self._libro = valor
    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, valor: Usuario):
        self._usuario = valor
