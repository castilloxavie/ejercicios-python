import random # libreria de numeros aleatorios.

def generar_contra():
    mayusculas = ['A', 'B', 'C',
    'D', 'E', 'F', 'G' ]
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']# se debe colocar tofdo el abecedario tanto en minusculas y marusculas
    simbolos = ['$', '/', '%', '|', '#', ')']
    numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] # se deben de colocar en forma caracteres los numeros

    caracteres = mayusculas + minusculas + simbolos + numero

    contrasena = [] # hacer una lista


    for i  in range(15):
        caracter_random =  random.choice(caracteres) # chois sirve para descoger un carater al azar
        contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)
    return contrasena
        


def run():
    contrasena =  generar_contra()
    print('tu nueva contrasena es: ' +  contrasena)



if __name__ == '__main__':
    run()