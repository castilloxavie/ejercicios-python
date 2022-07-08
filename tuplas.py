mi_primera_tupla=(18, 20, "maria", "camensa")

#mirar los pocisionamientos de los elementos de la tuplas

print(mi_primera_tupla[2])

#convertir una tupla en una lista (list)

miLista= list(mi_primera_tupla)
print(miLista)

#convertir una lista a tupla (tuple)
miLista= [18, 20,"maria", "camensa"]
miTupla=tuple(miLista)
print(miLista)

#averiguar cuantas veces se encuentra un elemento en mi tuplas (count)
miLista= [18, 20,"maria", "camensa"]
miTupla=tuple(miLista)
print(miTupla.count(18))

#ver la longitud de la tupla (len)
miLista= [18, 20,"maria", "camensa"]
miTupla=tuple(miLista)
print(len(miTupla))

#tuplas unitarias
mitupla=("xavier",)
print(len(mitupla))

#las tuplas no obligatoriamente debe de tener parentecis () esto se conoce como empaquetado de tuplas
tupla="javier", 17, "maria", 78.9
print(tupla)

#desempaquetado de tupla
tupla=("javier", 17, "maria", 78.9)
nombre, edad, apellido, numero=tupla
print(nombre)
print(edad)
print(apellido)
print(numero)

# debemos de tener encuenta q las tuplas son inmutables es decir q no se puede agregas nada, mover nada, eliminar nada
