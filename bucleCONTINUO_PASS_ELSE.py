# bucle con (continuo)
print("bucle con la intruccion CONTINUO")

for letra in "xavier":
    if letra=="i":
        continue
    print("viendo la letra: " + letra)
    
    
nombre= "pildoras de info"
contador= 0
for i in nombre:
    if i == " ":
        continue #el continue lo q hace es ignorar una linea de codigo.
    contador+=1

print(len(nombre))
print("aqui termina este programa")


#bucle con (PASS)
print("bucle con PASS")

while "true":
    pass

class numeros:
    pass # se utilizara mas tarde.
print("aqui termina este programa")


#bucle con (ELSE)
print("bucle con ELSE")

ima=input("escrimatu email")
for i in ima:
    if i=="@":
        arroba="true"
        break;
else:
    arroba="false"
print(arroba)    
