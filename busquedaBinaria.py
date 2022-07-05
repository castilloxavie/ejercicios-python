"""la busqueda binaria se encarga de acortar siempre las busqueda
por medio de siempre realizar una suma y una dicivion
la suma se hace por el alto y el bajo y se vivide siempre en 2
"""
inicio= int(input("ingrese su numero para identifcar: "))
aproximacion= 0.001
bajo=0.0 
alto= max (1.0, inicio)
resultado= ( alto + bajo) /2

while abs (resultado ** 2 - inicio) >= aproximacion:
    print(f'bajo={bajo}, alto={alto}, resutado={resultado}')
    if resultado **2  < inicio:
        bajo = resultado
    else:
        alto =resultado
        
    resultado = (alto + bajo) / 2  

print(f'la raiz cuadrarda de {inicio} es {resultado}')
