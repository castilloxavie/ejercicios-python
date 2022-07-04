from io import  open

archivo_texto=open("archivo.txt", "r") #la (r) es de lectura.
lineas_texto=archivo_texto.readlines() # este metodo (readlines()) sirve para convertir las lineas de texto  en una lista

archivo_texto.close()
print(lineas_texto)