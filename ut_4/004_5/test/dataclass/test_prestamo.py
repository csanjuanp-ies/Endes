import unittest
from datetime import datetime

from dataclass.Prestamo import Prestamo
from dataclass.Usuario import Usuario
from dataclass.Libro import Libro

class TestPrestamos(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario("a", "a", datetime.strptime("12/12/2022", '%m/%d/%Y'))
        self.usuario._id = 1
        self.libro = Libro("b", "b", 100)
        self.libro._id =1

    def test_create(self):
        prestamo_1 = Prestamo("c")
        prestamo_1.libro = self.libro
        prestamo_1.usuario = self.usuario
        self.assertEqual(str(prestamo_1),
                         "Libro:(1)b [b|100|]-Usuario:(1)a [a] |2022-12-12 00:00:00|(2023-02-06 00:00:00|None)")

    def test_prestamo_tarde(self):
        prestamo_1 = Prestamo("c")
        prestamo_1.libro = self.libro
        prestamo_1.usuario = self.usuario
        prestamo_1.fecha_de_prestamo = datetime(2022, 12, 12)
        prestamo_1.fecha_prevista_de_devolucion = datetime(2022, 12, 17)
        prestamo_1.cerrar_prestamo(datetime(2022, 12, 18))
        self.assertEqual(prestamo_1.devuelto_correcto, False)

    def test_prestamo_correcto(self):
        prestamo_1 = Prestamo("c")
        prestamo_1.libro = self.libro
        prestamo_1.usuario = self.usuario
        prestamo_1.fecha_de_prestamo = datetime(2022, 12, 12)
        prestamo_1.fecha_prevista_de_devolucion = datetime(2022, 12, 17)
        prestamo_1.cerrar_prestamo(datetime(2022, 12, 15))
        self.assertEqual(prestamo_1.devuelto_correcto, True)
        prestamo_1.cerrar_prestamo(datetime(2022, 12, 16))
        self.assertEqual(prestamo_1.devuelto_correcto, True)
        prestamo_1.cerrar_prestamo(datetime(2022, 12, 17))
        self.assertEqual(prestamo_1.devuelto_correcto, True)
