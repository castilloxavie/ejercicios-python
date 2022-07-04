import math #libreria de matematicas

def raiz_cuadrarda(listanumeros):
    """
    la funcion devuelve una lista con la
    raiz cuadrada de los elementos numericos
    pasador por parametro en otra lista
    
    se anida con los tres puntos (...)
    se puede hacer una excecion como en el ejemplo de la linea (17) asia abajo
    >>> lista=[]
    >>> for i in [4.9,16]:
    ...     lista.append(i)
    >>> raiz_cuadrarda(lista)
    [2.0, 3.0, 4.0]
    
    >>> lista=[]
    >>> for i in [4,-9,16]:
    ...     lista.append(i)
    >>> raiz_cuadrarda(lista)
    Traceback (most recet call last):
        ...     
    ValueError: math domain error
    
    """
    return[math.sqrt(n) for n in listanumeros]
    
#print (raiz_cuadrarda([9,19,25,36]))

import doctest
doctest.testmod()