diccionario= {
    'xavier':28,
    'daniel':26,
    'juan':25
}
print(diccionario)
print(diccionario['juan'])

print("------------------ejemplo de saber si esta esta lo q se busca en la lista o de lo contrario me devielve algo--------------------")
print(diccionario.get('marta', 'miente'))

print(diccionario.get('xavier', 'miente'))

print("------------cambiar datos  en el diccionario-----------------")
diccionario['juan']= 30
print(diccionario)

print("------------asignacion de otro elento al diccionario-------------")
diccionario["jose"]= 100
print(diccionario)

print("------------eliminar  elementos al diccionario-------------")
del diccionario['jose']
print(diccionario)

print("-------------------------iteracion  del diccionario------------------------------")
for llave in diccionario.keys():
    print(llave)

for valores in diccionario.values():
    print(valores)

for llaves, valores in diccionario.items():
    print(llaves, valores)

print("----------------------averiguacion  de llaves en nuestro diccionario------------------------------ ")
print('xavier' in diccionario)
print('chacela' in diccionario)
