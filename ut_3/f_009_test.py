from unittest import TestCase
from f_009 import calcular


class TestCalculo(TestCase):
    def test_calculara(self):
        self.assertEqual(calcular([1, 1, 1, 1, 1]), (0, 0, 5, 5))
        self.assertEqual(calcular([2, 2, 2, 2, 2]), (10, 5, 0, 0))
        #  En este momento ya está el 100% del código cubierto
        self.assertEqual(calcular([2, 1, 1, 1, 1]), (2, 1, 4, 4))
        self.assertEqual(calcular([2, 2, 2, 2, 1]), (8, 4, 1, 1))
        self.assertEqual(calcular([1, 1, 1, 1, 2]), (2, 1, 4, 4))
        self.assertEqual(calcular([1, 2, 2, 2, 2]), (8, 4, 1, 1))
        self.assertEqual(calcular([2, 2, 1, 1, 1]), (4, 2, 3, 3))
        self.assertEqual(calcular([2, 1, 1]), (2, 1, 2, 2))
        self.assertEqual(calcular([2]), (2, 1, 0, 0))
        self.assertEqual(calcular([1]), (0, 0, 1, 1))
        self.assertEqual(calcular([]), (0, 0, 0, 0))
