import math

def divide():
    try:
        op1=(float(input("introdusca su primer munero")))
        op2=(float(input("introdusca su segundo munero")))
        print("ladivicion es:  " + str(op1/op2))
    except ValueError:
        print("valor introducido es erroneo")
    except ZeroDivisionError:
        print("no se puede dividir por el 0")
    finally:
        
        print("calculo finalozado")
divide()

def evaluaEdad(edad):
    
    if edad <0:
        raise TypeError("no se permite edades negativas") # lanzamiento de error
    
    if edad<20:
        return "solo colagenos"
    elif edad <40:
        return "se agoto el colageno"
    elif edad <65:
        return "ere maduro"
    elif edad <100:
        return "ya estas comenzando a vivir h.e."
print(evaluaEdad(18))
print("aqui finalozado este programa")

print("programa de raiz cuadrada")

def raiz_cuadrada(num1):
    if num1<0:
        raise ValueError("el numero no puede se rnegativo")
    else:
        return math.sqrt(num1)
    
op1=int(input("ingrese un numero: "))
try:
    print(raiz_cuadrada(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
    
print("aqui termina este programa")