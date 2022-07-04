#bucles determinado (for)
for i in [1,2,3,]:
    print(i)
    
for  a in ["primavero", "verano","otoño","invierno"]:
    print(a)
    
for x in range(1,10):
    print(x)
    
    
    
# con  (end) hacemos q la impresion no lleve salto de linea al imprimir
for z in ["pildoras", "informatica", 3]:
    print("hello", end=' ')
    
    
    
#recorrido de concatenacion de caracteres o string
email="false"
miEmail=input("ingrese tu email por favor")
for c in miEmail:
    if(c=="@"):
        email="true"
if email=="true": 
    print("email es correcto")
else:
    print("no es correcto el email")
    

contador=0
mimi=input("coloque tu direccion electronica: ")
for aa in mimi:
    if(aa=="@" or aa=="."):
        contador=contador + 1
    
if contador==2: 
    print("email es correcto")
else:
    print("no es correcto el email")
    
    
#notaciones con el (print), (f) este caracter sirve para concatenar  str con variables
for xx in range(0,10,2):
    print(f"valor de la variable {xx}")
    
    
valido="false"
email=input("tu imail es: ")
for ss in range(len(email)):
    if email[ss]=="@":
        valido="true"
        
if valido:
    print("email correcto")
else:
    print("email incorrecto")