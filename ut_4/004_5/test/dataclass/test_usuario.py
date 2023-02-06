import unittest
from datetime import datetime
from dataclass.Usuario import Usuario

class TestUsuario(unittest.TestCase):
    def setUp(self):
        Usuario._next_id = 0

    def test_create(self):
        usuario_1 = Usuario("a","a",datetime.strptime("12/12/2022", '%m/%d/%Y'))
        self.assertEqual(str(usuario_1), "(1)a [a] |2022-12-12 00:00:00|")

    def test_igualdad(self):
        usuario_1 = Usuario("a", "a", datetime.strptime("12/12/2022", '%m/%d/%Y'))
        usuario_2 = Usuario("a", "a", datetime.strptime("12/12/2022", '%m/%d/%Y'))
        self.assertNotEqual(usuario_1, usuario_2)
        usuario_1._id = usuario_2._id
        self.assertEqual(usuario_1, usuario_2)

    def test_tipo(self):
        usuario_1 = Usuario("a", "a", datetime.strptime("12/12/2022", '%m/%d/%Y'))
        self.assertEqual(usuario_1.tipo, Usuario.TIPO["USUARIO"])
        usuario_1.tipo = "ADMINISTRADOR"
        self.assertEqual(usuario_1.tipo, Usuario.TIPO["ADMINISTRADOR"])
        usuario_1.tipo = "OTRO"
        self.assertEqual(usuario_1.tipo, Usuario.TIPO["ADMINISTRADOR"])

    def test_get_usuario_array(self):
        usuario_1 = Usuario("a", "a", datetime.strptime("12/12/2022", '%m/%d/%Y'))
        self.assertEqual(usuario_1.get_usuario_array(), ['a', 'a', datetime(2022, 12, 12, 0, 0)])