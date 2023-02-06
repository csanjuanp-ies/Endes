from almacenes.Usuarios import Usuarios
from almacenes.Editores import Editores
from almacenes.Libros import Libros
from almacenes.Prestamos import Prestamos
from dataclass.Usuario import Usuario
from dataclass.Editor import Editor
from dataclass.Libro import Libro
from dataclass.Prestamo import Prestamo
import datetime
class Libreria:
    def __init__(self):
        self._usuarios = Usuarios()
        self._libros = Libros()
        self._editores = Editores()
        self._prestamos = Prestamos()
    def cargar_usuarios(self):
        NOMBRE = 0
        DIRECCION  = 1
        FECHA_INGRESO = 2
        data = [
            ['Usuario 1', 'Dirección 1', datetime.datetime(2022,12,12)],
            ['Usuario 2', 'Dirección 2', datetime.datetime(2023, 12, 12)],
            ['Usuario 3', 'Dirección 3', datetime.datetime(2024, 12, 12)],
            ['Usuario 4', 'Dirección 4', datetime.datetime(2025, 12, 12)],
        ]
        for linea in data:
            self._usuarios.append(Usuario(linea[NOMBRE], linea[DIRECCION], linea[FECHA_INGRESO]))

    def cargar_libros(self):
        NOMBRE = 0
        DIRECCION = 1
        PRECIO = 2
        data = [
            ['Autor 1', 'Titulo 1', 100],
            ['Autor 2', 'Titulo 2', 200],
            ['Autor 3', 'Titulo 3', 300],
            ['Autor 4', 'Titulo 4', 400],
        ]
        for linea in data:
            self._libros.append(Libro(linea[NOMBRE], linea[DIRECCION], linea[PRECIO]))

    def cargar_editores(self):
        NOMBRE = 0
        DIRECCION = 1
        data = [
            ['Editor 1', 'Dirección 1'],
            ['Editor 2', 'Dirección 2'],
            ['Editor 3', 'Dirección 3'],
            ['Editor 4', 'Dirección 4'],
        ]
        for linea in data:
            self._editores.append(Editor(linea[NOMBRE], linea[DIRECCION]))
    def __str__(self):
        return f"usuarios:\n{self._usuarios}\n" + \
            f"editores:\n{self._editores}\n" + \
            f"libros:\n{self._libros}\n" + \
            f"Prestamos:\n{self._prestamos}"
