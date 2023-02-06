import unittest
from almacenes.Libros import Libros
from dataclass.Libro import Libro

class TestEditores(unittest.TestCase):
    def setUp(self):
        Libro._next_id = 0

    def test_crear(self):
        libros = Libros()
        self.assertEqual(str(libros), "[\n]")

    def test_add_editores(self):
        libros = Libros()
        editor_1 = Libro("a", "a", 100)
        libros.append(editor_1)
        self.assertEqual(str(libros), "[\n	[(1)a [a|100|]],\n]")


    def test_del_editores(self):
        libros = Libros()
        libros.append(Libro("a", "a", 100))
        libros.append(Libro("b", "b", 200))
        libros.remove(0)
        self.assertEqual(str(libros), "[\n	[(2)b [b|200|]],\n]")

    def test_iterator_editores(self):
        libros = Libros()
        texto = ""
        libros.append(Libro("a", "a", 100))
        libros.append(Libro("b", "b", 200))
        for libro in libros:
            texto += str(libro)
        self.assertEqual(texto, "(1)a [a|100|](2)b [b|200|]")