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
        self.usuarios = Usuarios()
        self.libros = Libros()
        self.editores = Editores()
        self.prestamos = Prestamos()

    def __str__(self):
        return f"usuarios:\n{self.usuarios}\n" + \
            f"editores:\n{self.editores}\n" + \
            f"libros:\n{self.libros}\n" + \
            f"Prestamos:\n{self.prestamos}"

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
            self.usuarios.append(Usuario(linea[NOMBRE], linea[DIRECCION], linea[FECHA_INGRESO]))

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
            self.libros.append(Libro(linea[NOMBRE], linea[DIRECCION], linea[PRECIO]))

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
            self.editores.append(Editor(linea[NOMBRE], linea[DIRECCION]))

    def hacer_prestamo(self, id_libro:int, id_usuario:int):
        libro = self.get_libro_from_id(id_libro)
        usuario = self.get_usuario_from_id(id_usuario)
        if libro is not None and usuario is not None and libro.disponible:
            self.prestamos.realizar_prestamo(libro , usuario)

    def devolover_libro(self, prestamo: int):
        prestamo = self.get_prestamo_from_id(prestamo)
        if prestamo is not None:
            self.prestamos.devolver_libro(prestamo)

    def get_prestamo_from_id(self, id_prestamo_a_buscar: int) -> Prestamo | None:
        if 0<= id_prestamo_a_buscar < len(self.prestamos):
            return self.prestamos[id_prestamo_a_buscar]

    def get_libro_from_id(self, id_libro: int) -> Libro | None:
        for libro in self.libros:
            if libro == id_libro:
                return libro

    def get_usuario_from_id(self, id_usuario: int) -> Usuario | None:
        for usuario in self.usuarios:
            if usuario == id_usuario:
                return usuario
