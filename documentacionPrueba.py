#hace pruebas de docomentacion
def area_triangulo(base,altura):
    """"
    calcula el area de un triangulo dados
    >>> area_triangulo (3,6)
    "el area del triangulo es: 9.0"
    esto nos sirve para saber si funciona nuestra aplicacion
    
    """
    return("el area del triangulo es: " + str(base*altura)/2)

import doctest
doctest.testmod()