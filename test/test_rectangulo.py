import unittest

from poligonos.rectangulo import area_rectangulo


class TestRectangulo(unittest.TestCase):

    def test_area_rectangulo_int(self):
        base = 8
        altura = 3

        area = area_rectangulo(base=base, altura=altura)
        self.assertEqual(area, 24)

    def test_Area_rectangulo_float(self):
        base = 1
        altura = 3.12345

        area = area_rectangulo(base=base, altura=altura)

        self.assertEqual(area, 3.12345)

    def test_area_rectangulo_base_invalida(self):
        base = 'hola'
        altura = 3

        with self.assertRaises(ValueError) as exc:
            area_rectangulo(base=base, altura=altura)

        self.assertEqual(str(exc.exception), 'base debe ser de tipo numerico')

    def test_area_rectangulo_altura_negativa(self):
        base = 2
        altura = -2

        with self.assertRaises(ValueError) as exc:
            area_rectangulo(base=base, altura=altura)

        self.assertEqual(str(exc.exception), 'altura debe ser un numero positivo')

# otra opcion de ejecutar es en terminal de pych : python -m unittest test.test_rectangulo
# gracias al llamando con el formato test_... el unittest reconoce donde ir   entonces seria en el termi
# python -m unittest
