import unittest
from almacenes.Editores import Editores
from dataclass.Editor import Editor

class TestEditores(unittest.TestCase):
    def setUp(self):
        Editor._next_id = 0

    def test_crear(self):
        editores = Editores()
        self.assertEqual(str(editores), "[\n]")

    def test_add_editores(self):
        editores = Editores()
        editor_1 = Editor("a", "a")
        editores.append(editor_1)
        self.assertEqual(str(editores), "[\n	[(1)a [a]],\n]")


    def test_del_editores(self):
        editores = Editores()
        editores.append(Editor("a", "a"))
        editores.append(Editor("b", "b"))
        editores.remove(0)
        self.assertEqual(str(editores), "[\n	[(2)b [b]],\n]")

    def test_iterator_editores(self):
        editores = Editores()
        texto = ""
        editores.append(Editor("a", "a"))
        editores.append(Editor("b", "b"))
        for editor in editores:
            texto += str(editor)
        self.assertEqual(texto, "(1)a [a](2)b [b]")