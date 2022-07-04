def compruebaEmail(usaurimail):
    """
    la funcion compruebaEmail evalua un mail
    recibe en busca del @. si tiene una @ es correcto
    si tiene mas de una @ es incorrectosi la @ esta al final es incorrecto
    
    >>> compruebaEmail('xavier@.com')
    True
    
    >>> compruebaEmail('xavier.com@')
    False
    
    >>> compruebaEmail('xavier.com')
    False
    
    >>> compruebaEmail('xavier@.com@')
    False
    
    """
    arraba=usaurimail.count('@')
    if (arraba!=1 or usaurimail.rfind('@')==(len(usaurimail)-1) or usaurimail.find('@')==0):
        return False
    else:
        return True
  
    
import doctest
doctest.testmod()

# aca se estan realizando pruebas con la documentacion si el programa esta bien o mal
# debes de saber q cuando lo ejecute y no sale nada eso quiere decir q esta bn  o lo contrario si sale  failed eso quiere desir q esta mal