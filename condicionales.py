print("programa de evaluacion de alumnos")

nota_alumno=input("introdusca su nota por favor: ")

def evaluacion (nota):
    valoracio="aprobado"
    if nota<5:
        valoracio= "reprovado"
    return valoracio

print(evaluacion(int(nota_alumno)))
print("termina el programa")

# condicional if  else elif 
print("programa para ver si es mayor de edad o no ")
edad_usuari=int(input("introdusca tu edad: "))

if edad_usuari<18:
    print("no puedes pasar")
elif edad_usuari > 100:
    print("edad incorrecta")
else:
    print("bienvenido")

print("termina el programa")


#condicional con concatenacion  de operadores  de comparacion
print("otro programa de condicional")

edad=9
if 0< edad < 100:
    print("edad es correcta")
else:
    print("edad incorrecta")


print("termina el programa")


#ejemplo
print("evaluar el salario de diferentes sectoresd e la empresa")

salariopresidente=int(input("intrudusca el salario del presidente: "))
print("salario presidente: " + str(salariopresidente))

salariodirector=int(input("intrudusca el salario del director: "))
print("salario presidente: " + str(salariodirector))

salariojefearea=int(input("intrudusca el salario del jefe de area: "))
print("salario presidente: " + str(salariojefearea))

salarioadministrativo=int(input("intrudusca el salario administrativo: "))
print("salario presidente: " + str(salarioadministrativo))

if salarioadministrativo<salariojefearea<salariodirector<salariopresidente:
    print("todo funciona correctamente")
else:
    print("algo esta mal")
    
print("termina el programa")

