from dataclass.Libro import Libro
from dataclass.Usuario import Usuario
from datetime import datetime, timedelta

class Prestamo:
    DIAS_DE_PRESTAMO_POR_DEFECTO = timedelta(days=5)
    def __init__(self, asunto:str):
        self._libro:Libro|None = None
        self._usuario:Usuario|None = None
        self.asunto:str = asunto
        fecha_actual = datetime.now()
        self.fecha_de_prestamo:datetime = datetime(fecha_actual.year, fecha_actual.month, fecha_actual.day)
        self.fecha_prevista_de_devolucion:datetime = self.fecha_de_prestamo + Prestamo.DIAS_DE_PRESTAMO_POR_DEFECTO
        self.fecha_de_devolucion: datetime|None = None

    def __eq__(self, other:"Prestamo"):
        return self._libro == other._libro and \
            self._usuario == other._usuario and \
            self.fecha_de_prestamo == other.fecha_de_prestamo
    def __str__(self):
        return f"Libro:{self._libro}-Usuario:{self.usuario}" + \
            f"({self.fecha_de_prestamo}|{self.fecha_de_devolucion})"

    @property
    def libro(self):
        return self._libro
    @libro.setter
    def libro(self, valor: Libro):
        self._libro = valor
        self._libro.disponible = False
    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, valor: Usuario):
        self._usuario = valor
    @property
    def devuelto_correcto(self)->bool|None:
        if self.fecha_de_devolucion is not None:
            return self.fecha_prevista_de_devolucion >= self.fecha_de_devolucion
        return None
    def cerrar_prestamo(self, fecha_devolucion:datetime|None):
        if fecha_devolucion is None:
            fecha_actual = datetime.now()
            self.fecha_de_devolucion = datetime(fecha_actual.year, fecha_actual.month, fecha_actual.day)
        else:
            self.fecha_de_devolucion = datetime(fecha_devolucion.year, fecha_devolucion.month, fecha_devolucion.day)

        self._libro.disponible = True
