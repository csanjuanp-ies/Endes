import unittest
from dataclass.Libro import Libro
from dataclass.Editor import Editor

class TestUsuario(unittest.TestCase):
    def setUp(self):
        Libro._next_id = 0

    def test_create(self):
        libro_1 = Libro("a","a", 100)
        self.assertEqual(str(libro_1), "(1)a [a|100|]")

    def test_igualdad(self):
        libro_1 = Libro("a", "a", 100)
        libro_2 = Libro("a", "a", 100)
        self.assertNotEqual(libro_1, libro_2)
        libro_1._id = libro_2._id
        self.assertEqual(libro_1, libro_2)

    def test_get_usuario_array(self):
        libro_1 = Libro("a", "a", 100)
        self.assertEqual(libro_1.get_libro_array(), ['a', 'a', 100, True, None])

    def test_publicado_por(self):
        libro_1 = Libro("a", "a", 100)
        editor_1 = Editor("b", "b")
        libro_1.publicado_por = editor_1
        self.assertEqual(libro_1.get_libro_array(), ['a', 'a', 100, True, "b"])
        libro_2 = Libro("a", "a", 100)
        libro_1.publicado_por = libro_2
        self.assertEqual(libro_1.get_libro_array(), ['a', 'a', 100, True, "b"])
