def run():
    diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }


    #print(diccionario['llave1'])  #ca hacemos lo q se hace es mostrar lo q tiene
    #print(diccionario['llave2'])  # cada llave.
    #print(diccionario['llave3'])


    poblacion_paises = {
        'argentina':5460003489,
        'brasil':2108364648290,
        'colombia':50000000,
    }
    #print(poblacion_paises['argentina'])
    #print(poblacion_paises['brasil'])
    #rint(poblacion_paises['colombia'])

    #for pais in poblacion_paises.keys():
       # print(pais)

    #for pais in poblacion_paises.values():
     #   print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes') 


if __name__ == '__main__':
    run()
