miDiccionario={"alemania":"berlin", "francia":"paris", 27:"londres", "esoaña":72, "colombia":"bogota"}

#como acceder a un elelmnto del diccionario se hace por la clave para obtener el valor
print(miDiccionario["colombia"])

#accedder a todod mi diccionario
print(miDiccionario)

#agregar mas elementos a mi diccionariodos
miDiccionario["venezuela"]="caracas"
print(miDiccionario)

#modificar un valor a una clave q fue erronea
miDiccionario["venezuela"]="caraquillas"
print(miDiccionario)

#eliminar elementos (del)
del miDiccionario["venezuela"]
print(miDiccionario)

#podemos tarer tambien una tupla con las clavesy luego se le coloca los valore
mi_tupla= ["españa", "francia","reino unido", "alemania"]
miDiccionario={mi_tupla[0]:"madril", mi_tupla[1]:"paris", mi_tupla[2]:"londres", mi_tupla[3]:"berlin"}
print(miDiccionario)

#almacenar una tupla en un diccionario
miDiccionario={23:"emelin", "nombre":"emeli", "ocupacion":"ama de casa","compromisos":[190, 1993, 2003, 2006]}
print(miDiccionario)
print(miDiccionario["ocupacion"])
print(miDiccionario["compromisos"])

#un diccionario dentro de otro
miDiccionario={23:"emelin", "nombre":"emeli", "ocupacion":"ama de casa","compromisos":{"nacimientos":[190, 1993, 2003, 2006]}}
print(miDiccionario["compromisos"])

#metodos para las claves (keys)
print(miDiccionario.keys())

#mirar todos los valores de las claves (values)
print(miDiccionario.values())

#ver la longitud de nuestro diccionariodos
print(len(miDiccionario))