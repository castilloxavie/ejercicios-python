# el metodo (match) sirve para para buscar al principio de las cadenas de caracteres si hay o no hat coincidencia
import re
nom= "xavier alberto castillo"
nom1= "emelina varon ochoa"
nom2= " alberto castillo hernandez"
nom3= "Xavier alberto castillo"


if re.match("xavier",nom3, re.IGNORECASE): # el metocaracter (match) sirve para encontrar al principo las coincidencias de caracteres tambien acepta tercer parametro y es (IGNORECASE)esto sirve para q no respete mayusculas y minusculas
    print("hemos encontrado una coincidensia")
else:
    print("no se a encontrado ninguna coincidensia")

nomo= "jara lopez"
nomo1= "lara lopez"

if re.match(".ara", nomo1, re.IGNORECASE):
     print("hemos encontrado una coincidensia en la variable")
else:
    print("no se a encontrado ninguna coincidensia en la variable")

cadena="xavier"
cadena1="1234567890"
cadena2="a1234567890"

if re.match("\d", cadena1): # el metodo ("\d") sirve paqra buscar numeros q esten dentro de una cadena de caracteres o un str(string)
    print("hemos encontrado una coincidensia")
else:
    print("no se a encontrado ninguna coincidensia")




# el metodo (search) sirve para para buscar entodas las cadenas de caracteres si haoy coincidencio o no hay
nomo= "jara lopez"
nomo1= "lara lopez"

if re.search("lopez", nomo1, ):
     print("hemos encontrado una coincidensia en la variable")
else:
    print("no se a encontrado ninguna coincidensia en la variable")
  

