import pickle

fichero=open("ls_nombre", "rb") # la (rb) lectura binaria

lista=pickle.load(fichero) # la palabra reservada (load) sirve para  nuevamente cargar o recurar.

print(lista)