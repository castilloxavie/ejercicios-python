# las funciones (filter)son de orden superior
#verificar q  los elements de una secuencia cumplen una condicion
#devolviendo un iterador con los elementos q cumplen dicha condicion.

"""def numero_para(num):
    if num % 2==0:
        return True

numeros=[17,24,7,39,8,51,92]
print(list(filter(numero_para, numeros)))"""

numeros=[17,24,7,39,8,51,92]
print(list(filter(lambda numero_par:numero_par%2==0, numeros)))


#la funcion filter sirve para filtrar objetos 
print ("otros ejemplos")

class empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo= cargo
        self.salario=salario
    def __str__(self):
        return "{} q trabaja como {} tiene salario de  $ {}".format(self.nombre, self.cargo, self.salario)
    
empleadosLista=[
   empleado("xavier", "operario,", 30000),
   empleado("ana", "presidenta,", 50000),
   empleado("juan", "administrador,", 400000),
   empleado("alberto", "secretaria,", 35000),

]
salario_altos=filter(lambda empleado:empleado.salario>35000, empleadosLista )
for empleados_salario in salario_altos:
    print(empleados_salario)
