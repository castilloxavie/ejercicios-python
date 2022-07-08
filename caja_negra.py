"""
Las pruebas de caja negra se definen como una técnica de testing en la que se prueba la 
funcionalidad de una aplicación ignorando la parte interna de dicha aplicación.
"""

import unittest


def suma(num1, num2):
    return abs(num1) + num2


class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num1 = 10
        num2 = 5

        resultado = suma(num1, num2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num1 = -10
        num2 = -7

        resultado = suma(num1, num2)

        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()
