import random # esta es una libreria q nos ayuda a traer numeros aleatorios 
              # para poder ejecutar nuestro juego

def run():
    numero_aleatorio =random.randint(1, 100)
    numero_elegido = int(input('ingrese un nemero de l 1 al 100: ') )
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('busca un nemero mayor')
        else:
            print('busque un numero menor')
        numero_elegido = int(input('elija nuevamente un numero: ')) #debemos de tener en cuenta cuando coloquemos la variable 
                                                                    # numero_elegido que debe de quedar a la alineacion deñl if 
                                                                    #y no del else ya q tendriamos un bucle infinito.
      
    print('¡ganaste')


if __name__ == '__main__':
    run()