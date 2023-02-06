from dataclass.Libro import Libro
from dataclass.Usuario import Usuario
from datetime import datetime, timedelta

class Prestamo:
    DIAS_DE_PRESTAMO_POR_DEFECTO = timedelta(days=5)
    def __init__(self, asunto:str):
        self._libro:Libro|None = None
        self._usuario:Usuario|None = None
        self.asunto:str = asunto
        self.fecha_de_prestamo:datetime = datetime.now()
        self.fecha_prevista_de_devolucion:datetime = self.fecha_de_prestamo + Prestamo.DIAS_DE_PRESTAMO_POR_DEFECTO
        self.fecha_de_devolucion: datetime|None = None

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
    @property
    def devuelto_tarde(self):
        if self.fecha_de_devolucion is not None:
            return self.fecha_prevista_de_devolucion <= self.fecha_de_devolucion
        return None
    def cerrar_prestamo(self):
        self.fecha_de_devolucion = datetime.now()
