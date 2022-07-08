import pickle # con esta librerio de py sirve para codificar de forma binaria lo q usted  desee 

ls_nombre=["xavier", "alberto","emelina", "alexis", "yuliana", "anyi", "paola", "norma", "edit", "shopia", "dapne", "nuray"]

fichero_binario=open("ls_nombre","wb") #la combinacion de (wb) esto es escritura binaria

pickle.dump(ls_nombre, fichero_binario ) # la palabra reservada (dump) sirve para volcar o colocar la informacion donde nosotros la programemos.
fichero_binario.close()

del(fichero_binario)