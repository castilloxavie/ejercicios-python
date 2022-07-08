import re

cadena= "vamos con toda a aprender la expreciones regulares en python. python es un lenguaje de sintaxis sencilla y con un alto nivel para el mundo laboral"
"""
textoBuscar="aprender"
textoEncontrado=re.search(textoBuscar,cadena)

print(textoEncontrado.start())#el metodo (start) sirve para decirnos donde comienza lo q se esta buscando dentro del texto
print(textoEncontrado.end()) #el metodo (end) sirve para decir donde finaliza lo q se esta buscando en en el texto
print(textoEncontrado.span())#el metodo (span) sirve para mostrar donde comienza y donde termina lo q se esta buscando, tambien lo muestra en forma de tupla."""

textbuscar="python"
print(re.findall(textbuscar, cadena)) # el metodo (findall) sirve para encontrar las coincidencias en el texto y lo presenta en forma de lista
print(len(re.findall(textbuscar, cadena))) # el metodo (len) sirve para decir cuantas veces se a encontrado coincidencias  dentro de un texto
