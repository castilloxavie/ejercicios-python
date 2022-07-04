import math # importacion de librerio o clase para hacer operaciones matematicas ejemplo raiz cuadrada.

#bucles indeterminados(while)
x=1
while x<=10:
    print("ejecucion" + str(x))
    x=x+1
print("termina la ejecucion")
print("aqui termina este programa")



print("programa de edades")
edad=int(input("escriba tu edad: "))
while edad<0:
    print("has introducido una edad incorecta....")
    edad=int(input("escriba tu edad: "))

print("gracias ingrese")
print("la edad es: " +str(edad)+ " años")
print("aqui termina este programa")
    
    
    
print("programa de edades y comparaciones")
edad=int(input("escriba tu edad: "))
while edad<10 or edad>100:
    print("has introducido una edad incorecta....")
    edad=int(input("escriba tu edad: "))

print("gracias ingrese")
print("la edad es: " +str(edad)+ " años")
print("aqui termina este programa")


# en este ejemplo asi while sea indeterminado se puede programar para q tenga fin y no se quede hay en un ciclo infinito 
print("averiguar la raiz cuadradea de un numero")
numero= int(input("introdusca un numero: "))
intentos=0

while numero<0:
    print("no se puede hallar la raiz cuadrada de un numero negativo")
    
    if numero==2: 
        print("has consumidos la cantidade de intentos")
        break;
    
    numero= int(input("introdusca un numero"))
    if numero<0:
        intentos=intentos+1
        
if intentos<2:
    solucion=math.sqrt(numero)
    print("raiz cuadrada de " +str(numero) + " es " + str(solucion))
    print("aqui termina este programa")
