#condicionales con operadores logicos and y or. operador in
print("evaluar nota de un alumno para saber si puede obtener una beca o no")

distancia_escuela=int(input("intrudusca la distancia de la casa a la escuela en km: "))
print("la distancia es " + str(distancia_escuela) + " km")

numero_hermanos=int(input("cuantos hermanos tienes: "))
print("la cantidad de hermnos son: " + str(numero_hermanos))

salario_familiar=int(input("cual es sel salario anual de la familia: "))
print("el salario de la familia es: " +str(salario_familiar))

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("tienes derecho a una beca")
else:
    print("no tienes derecho a beca")


print("termina el programa")

#condicional con (or)
print("evaluar nota de un alumno para saber si puede obtener una beca o no")

distancia_escuela=int(input("intrudusca la distancia de la casa a la escuela en km: "))
print("la distancia es " + str(distancia_escuela) + " km")

numero_hermanos=int(input("cuantos hermanos tienes: "))
print("la cantidad de hermnos son: " + str(numero_hermanos))

salario_familiar=int(input("cual es sel salario anual de la familia: "))
print("el salario de la familia es: " +str(salario_familiar))

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("tienes derecho a una beca")
else:
    print("no tienes derecho a beca")


print("termina el programa")

#condicional con (in)
print("asignatura opcional")

print("las materias opcionales son: informatica grafica, prueba de software, usabilidad y accebilidad ")
opcion=input("escriba laasignatura escogida")

asignatura=opcion.lower() # lower sirve para colocar todo en minuscula

if asignatura in("informatica grafica", "prueba de software", "usabilidad y accebilidad"):
    print("asignatura elegida"+ asignatura)
else:
    print("la asignatura escogida no esta en el pensul de materias opcionales.")