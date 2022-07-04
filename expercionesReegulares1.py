#herramientas. las expersiones regulares son una
#secuencia de caracteres q formanun patron de busqueda.
#sirve para trabajos de procesamientos de texto

import re #librerioa para trabajar las expeciones regulares

cadena= "vamos con toda a aprender la expreciones regulares"
#print(re.search("aprender", cadena))
textoBuscar="aprender"
if re.search(textoBuscar,cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado nada en el texto")