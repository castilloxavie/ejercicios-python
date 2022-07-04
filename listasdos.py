mi_primera_lista=["xavier", "alberto", "pepep", "emelina", "true", 45.78]

#agragar elementos en las listas con (append)

mi_primera_lista.append(16)

#agragar elementos en las listas en punto indicado por el programador es con (insert)

mi_primera_lista.insert(3,"angyi")

#agregar varios elementos a mi lista utilizo (extend)

mi_primera_lista.extend([30, "hola", "mundo"])

#como devolver el indice del elemento en cuestion  (index)

print(mi_primera_lista.index("mundo"))

#comprobar si esta un elemento en nuestra lista (in)

print("yyuliana" in mi_primera_lista)

#eliminar elementos de tu lista (remove)

mi_primera_lista.remove("xavier")

#eliminar el ultimo elemento de la lista (pop)

mi_primera_lista.pop()

#tambien se puede unir varias listas con una tercera  ejemplo  miLista1, miLista2  miLista3 seria la union de las doa anteriores liasta con el sino (+)

print(mi_primera_lista[:])

print(mi_primera_lista[3])

print(mi_primera_lista[2])

print(mi_primera_lista[-1])

print(mi_primera_lista[0:3])

print(mi_primera_lista[:3])

print(mi_primera_lista[1:3])

print(mi_primera_lista[3:])