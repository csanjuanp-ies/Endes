import unittest
from datetime import datetime

from almacenes.Prestamos import Prestamos
from dataclass.Libro import Libro
from dataclass.Prestamo import Prestamo
from dataclass.Usuario import Usuario


class TestUsuarios(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario("a", "a", datetime.strptime("12/12/2022", '%m/%d/%Y'))
        self.usuario._id = 1
        self.libro = Libro("b", "b", 100)
        self.libro._id = 1

    def test_crear(self):
        prestamos = Prestamos()
        self.assertEqual(str(prestamos), "[\n]")

    def test_add_prestamos(self):
        prestamos = Prestamos()
        prestamo = Prestamo("a")
        prestamo.fecha_de_prestamo = datetime(2022, 12, 12)
        prestamo.fecha_de_devolucion = datetime(2022, 12, 12)
        prestamo.libro = self.libro
        prestamo.usuario = self.usuario
        prestamos.append(prestamo)
        self.assertEqual(str(prestamos), "[\n	[Libro:(1)b [b|100|]-Usuario:(1)a [a] |2022-12-12 00:00:00|(2022-12-12 00:00:00|2022-12-12 00:00:00)],\n]")


    def test_del_usuarios(self):
        prestamos = Prestamos()
        prestamo = Prestamo("a")
        prestamo.fecha_de_prestamo = datetime(2022, 12, 12)
        prestamo.fecha_de_devolucion = datetime(2022, 12, 12)
        prestamo.libro = self.libro
        prestamo.usuario = self.usuario
        prestamos.append(prestamo)
        prestamo = Prestamo("b")
        prestamo.fecha_de_prestamo = datetime(2022, 12, 12)
        prestamo.fecha_de_devolucion = datetime(2022, 12, 12)
        prestamo.libro = self.libro
        prestamo.usuario = self.usuario
        prestamos.append(prestamo)
        prestamos.remove(0)
        self.assertEqual(str(prestamos), "[\n	[Libro:(1)b [b|100|]-Usuario:(1)a [a] |2022-12-12 00:00:00|(2022-12-12 00:00:00|2022-12-12 00:00:00)],\n]")

    def test_iterator_usuarios(self):
        prestamos = Prestamos()
        texto = ""
        prestamo = Prestamo("a")
        prestamo.fecha_de_prestamo = datetime(2022, 12, 12)
        prestamo.fecha_de_devolucion = datetime(2022, 12, 12)
        prestamo.libro = self.libro
        prestamo.usuario = self.usuario
        prestamos.append(prestamo)
        prestamo = Prestamo("b")
        prestamo.fecha_de_prestamo = datetime(2022, 12, 12)
        prestamo.fecha_de_devolucion = datetime(2022, 12, 12)
        prestamo.libro = self.libro
        prestamo.usuario = self.usuario
        prestamos.append(prestamo)
        for usuario in prestamos:
            texto += str(usuario)
        self.assertEqual(texto, "Libro:(1)b [b|100|]-Usuario:(1)a [a] |2022-12-12 00:00:00|(2022-12-12 00:00:00|2022-12-12 00:00:00)Libro:(1)b [b|100|]-Usuario:(1)a [a] |2022-12-12 00:00:00|(2022-12-12 00:00:00|2022-12-12 00:00:00)")