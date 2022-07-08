# las cadenas de caracteres para paithon son (string)
nombre=input("ingrese su nombre")
print("el nombre es: ", nombre.upper())# sirve para cambiara de minuscula a mayuscula
print("el nombre es: ", nombre.lower())#sirve para cambiar de mayuscula a minusculas
print("el nombre es: ", nombre.capitalize())#sirve para colocar la primera letra o vocal en mayuscula

edad=input("ingrese tue edad")
print(edad.isdigit())# este es un booleano q sirve pasa saber si esl falso o verdadero

while(edad.isdigit()==False):
    print("ingrese un valor numerico")
    edad=input("ingrese tue edad")
    
if (int(edad)<18):
    print("no puede pasar")
else:
    print("puedes pasar")