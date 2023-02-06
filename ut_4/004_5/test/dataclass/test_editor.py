import unittest
from dataclass.Editor import Editor

class TestUsuario(unittest.TestCase):
    def setUp(self):
        Editor._next_id = 0

    def test_create(self):
        editor_1 = Editor("a","a")
        self.assertEqual(str(editor_1), "(1)a [a]")

    def test_igualdad(self):
        editor_1 = Editor("a", "a")
        editor_2 = Editor("a", "a")
        self.assertNotEqual(editor_1, editor_2)
        editor_1._id = editor_2._id
        self.assertEqual(editor_1, editor_2)

    def test_get_usuario_array(self):
        editor_1 = Editor("a", "a")
        self.assertEqual(editor_1.get_editor_array(), ['a', 'a'])