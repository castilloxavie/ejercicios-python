def factoriales(x):
    """
    calcular el factorial de x
    n int > 0
    retur x!
    """
    print(x)
    
    if x ==1:
        return 1

    return x * factoriales (x -1)

x =int(input("escriba un numero: "))
print(factoriales(x))
        
    