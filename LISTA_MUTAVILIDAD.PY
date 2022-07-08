from re import M
from tokenize import Double


my_list = [1, 2, 3, 3]
print(my_list[0])
print(my_list[2:])

print("-------------modificaciones a la lista  con append------------")
my_list.append(4)
print(my_list)

print("modificar lista ")
my_list[0]= "xavier"
print(my_list)

print("------------quitar un elemento de las listas y modificar con pop-----------")
my_list.pop(3)
print(my_list)

print("iteracion de mi lista")
for elemento in my_list:
    print(elemento)

print("----------efectos secundarios de las listas-------------")

milistica= [1,2,3,4,5,6,7,8,9,]
b=milistica
print(milistica)
print(b)

print("-------se esta apuntando al misimo lugar es decir q solo hay una lista-----------")

print(id(milistica))
print(id(b))

print("-----lista de comparacion de los efectos secundarios o errores q nos e deben de hacer-------")

c=[milistica, b]
print(c)

milistica.append(10)
print(milistica)
print(c)

print("---------clonacion de  listas---------------")

x=["xavier", "alberto", "casrillo", "varon"]
c=x
v=list(x)
print(x)
print(v)
print("la id de las listas")
print(id(x))
print(id(c))
print(id(v))

print("otra forma de clonar")
d = x [::]
print(d)
print(id(d))

print("------------listas  de comprencio------------")

lisa=list(range(100))
print(lisa)

print("------------------------------------------------------------------------")

double=[i *2 for i in lisa]
print(double)

print("sacar los numeros pares de la lista")
pares=[i for i in lisa if i % 2==0]
print(pares)

print("sacar los numeros impares o nones de la lista")
inpar=[i for i in lisa if i % 2!=0]
print(inpar)
