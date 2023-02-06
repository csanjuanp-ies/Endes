import unittest
from datetime import datetime

from almacenes.Usuarios import Editores
from dataclass.Usuario import Usuario

class TestUsuarios(unittest.TestCase):
    def setUp(self):
        Usuario._next_id = 0

    def test_crear(self):
        usuarios = Editores()
        self.assertEqual(str(usuarios), "[\n]")

    def test_add_usuarios(self):
        usuarios = Editores()
        usuario_1 = Usuario("a", "a", datetime.strptime("12/12/2022", '%m/%d/%Y'))
        usuarios.append(usuario_1)
        self.assertEqual(str(usuarios), "[\n	[(1)a [a] |2022-12-12 00:00:00|],\n]")


    def test_del_usuarios(self):
        usuarios = Editores()
        usuarios.append(Usuario("a", "a", datetime.strptime("12/12/2022", '%m/%d/%Y')))
        usuarios.append(Usuario("b", "b", datetime.strptime("12/12/2022", '%m/%d/%Y')))
        usuarios.remove(0)
        self.assertEqual(str(usuarios), "[\n	[(2)b [b] |2022-12-12 00:00:00|],\n]")

    def test_iterator_usuarios(self):
        usuarios = Editores()
        texto = ""
        usuarios.append(Usuario("a", "a", datetime.strptime("12/12/2022", '%m/%d/%Y')))
        usuarios.append(Usuario("b", "b", datetime.strptime("12/12/2022", '%m/%d/%Y')))
        for usuario in usuarios:
            texto += str(usuario)
        self.assertEqual(texto, "(1)a [a] |2022-12-12 00:00:00|(2)b [b] |2022-12-12 00:00:00|")