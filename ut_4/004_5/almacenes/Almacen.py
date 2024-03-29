from dataclass.Editor import Editor
from dataclass.Libro import Libro
from dataclass.Prestamo import Prestamo
from dataclass.Usuario import Usuario


class Almacen:
    def __init__(self, titulo:str=""):
        self.titulo = titulo
        self._objetos = []

    def __len__(self):
        return len(self._objetos)

    def __iter__(self):
        return iter(self._objetos)

    def __getitem__(self, item):
        if 0 <= item < len(self._objetos):
            return self._objetos[item]
        return None

    def append(self, other:Libro|Prestamo|Editor|Usuario):
        self._objetos.append(other)

    def remove(self, index:int):
        if 0 <= index < len(self._objetos):
            del self._objetos[index]
