from io import  open
# posicionamiento del puntero en nuestr archivo txt
archivo_texto=open("archivo.txt", "r+") # sirve para leer y escritura
archivo_texto.write("comienzo de texto")
print(archivo_texto.read()) # con (read()) tambien nons sirve para leer hasta donde se le haya pasado el parametro

archivo_texto. seek() # con la palabra reservada de py  (seek()) nos sirve para colocar el puntero donde uste desee.
# debemos de tener en cuenta q si la palabra reservada q estamos trabajando en esta funcionalidad de py la colocamos antebtes del print
# en la consola leera despues del parametro q le haya colocado.

archivo_texto.seek(len(archivo_texto.read())/2) # sirve para mostrarnos la mitad del archivo
archivo_texto.seek(len(archivo_texto.readlines())) # sirve para empesar a leer de donde usted quiera.

ls_testo=archivo_texto.readlines();

ls_testo[1]="esta linea a sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(ls_testo)
archivo_texto.close()