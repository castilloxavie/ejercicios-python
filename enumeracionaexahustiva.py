obgetivo= int(input("ingrese el numero a verificar: ") )
resultado =0

while resultado **2 < obgetivo:
    print(resultado)
    resultado +=1
    
if resultado **2 == obgetivo:
    print(f'la rais cuadrada del  {obgetivo} es {resultado}')
    
else:
    print(f'el {obgetivo} no tiene raiz cuadrada exacta')
