def palindromo(palabra):
    palbra = palabra.replace('', '')
    palabra = palabra.lower()
    palbra_invertida = palbra[::-1]
    if palabra == palbra_invertida:
        return True
    else:
        return False


def rum():
    palabra = input('escriba una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('es palindromo')
    else:
        print('no es palindromo')



if __name__ == '__main__':
    rum()