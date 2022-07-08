"""
Las pruebas de caja blanca (también conocidas como pruebas de caja de cristal o pruebas estructurales)  
se centran en los detalles procedimentales del software,
por lo que su diseño está fuertemente ligado al código fuente, lo cual, 
esto significa que tenemos que realizar un “estudio”, o más bien, un análisis de nuestro codig

"""
import unittest


def es_mayor_de_edad(edad):
    if edad >= 18:
        return False
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()

    
    """
    denbemos de tener en cuenta cuan hagamos las apreciaciones con el False y e True para realizar 
    el test.

    """