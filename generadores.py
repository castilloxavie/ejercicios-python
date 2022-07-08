#bucle con procesos tradicionales
print("funcion de numeros pares tradicional")

def pares(limite):
    num=1
    mimista=[]
    
    while num<limite:
        mimista.append(num*2)
        num=num+ 1
        
    return mimista
print(pares(100))
print("aqui termuna este programa")


#bucle con generadores (yield)
print("bucles con generadores (yield) ")

def pares(limite):
    num=1
    
    while num<limite:
        yield num*2
        num=num+ 1
devuelvepares= pares(10)   
   
for i in devuelvepares:
    print(i)
print("aqui termuna este programa")


#bucle con generadores (yield) y (next) next sirve para llamar uno a uno lo q esta almacenado en su variable.
print("bucles con generadores (yield) y (next) ")

def pares(limite):
    num=1
    
    while num<limite:
        yield num*2
        num=num+ 1
devuelvepares= pares(10)   
print(next(devuelvepares))
print("aqui podria ir mas codigo...")
print(next(devuelvepares)) 

print("aqui podria ir mas codigo...")
print(next(devuelvepares)) 

print("aqui termuna este programa")

    