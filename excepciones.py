# la excepciones son la en cargadadas de ayudar si depronto a la hora  de la ejecucion del codigo presente una falla  este se encarga de seguir corriendo el programa y q no se caiga de donde encontro el error de ejecucioan hacia abajo.
import re


def suma(num1, num2):
    	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:		
	    return num1/num2
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
        return "operacion erronea"
while "true":	
    try:
        op1=(int(input("Introduce el primer numero: ")))
        op2=(int(input("Introduce el segundo numero: ")))	
        break;	
    
    except ValueError:
        print("los valores introduccidos no son corecctos")	
    
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")