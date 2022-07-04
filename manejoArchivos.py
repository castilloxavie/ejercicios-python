from io import open # esto basicamente sirve para abrir archivos externos. para abrirlos en solo lectura, en escritura o agregar mas informacio

archivo_texto=open("archivo.txt", "w")# la (W)es de modo escritura.
frase="es un estupendo y bello dia \n es sabado"

archivo_texto.write(frase)

archivo_texto.close()
#archivo_texto=open("archivo.txt", "r") #la (r) es de lectura.
#texto=archivo_texto