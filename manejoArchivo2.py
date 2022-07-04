from io import  open

archivo_texto=open("archivo.txt", "r") #la (r) es de lectura.
texto=archivo_texto.read()

archivo_texto.close()
print(texto)