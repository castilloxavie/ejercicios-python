# las expreciones reguares o metacracteres don de se ven anclas 
#y clases de cararcteres
import re

lista_nombres=[
    "xavier castillo",
    "emelina varon",
    "norma varo",
    "alberto castillo",
    "emelina ochoa"
]
# estos metacareacteres sirven tambienpara buscar dominios q se encuentren en un lista de su aplicacion.
for elementos in lista_nombres:
    if re.findall("^emelina", elementos): #el metacaracter (^)sirve para buscar las coincidencias dentro de una lista q comienza por los caracteres q se establecen
        print(elementos)
        
for elementos1 in lista_nombres:
    if re.findall("castillo$", elementos1):# el metacaracter ($)sirve para buscar todos los q termineb con la coincidencia de caracteres.
        print(elementos1)
        
        
# clase de caracteres dentro de un texto
listas_nombres=[
    "xavier castillo le gusta la mañana",
    "emelina varon am la piña",
    "norma varo piñan",
    "alberto castillo siempre pide la ñapa",
    "emelina ochoa le dicen la ñaña",
    "niñas",
    "niños",
    "otro ejemplo ññ"
]

for elementos3 in listas_nombres:
    if re.findall("[ñ]", elementos3):
        print(elementos3)
        
for elementos4 in listas_nombres:
    if re.findall("niñ[oa]s", elementos4): # el metacaracter como esta en el ejemplo ("niñ[oa]s") sirve para buscar en la lista las cioncidencias q ya esta en el parametro.
        print(elementos4)