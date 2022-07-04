#aplica una funcion a cada elemento de un a lista  iterable(lista, tuplas) devolviendo una lista con el resultado.
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

def calculo_comision(empleado):
    if(empleado.salario<=400000):
        empleado.salario=empleado.salario*1.03
    return empleado

listaEmpleComision=map(calculo_comision,empleadosLista)
for empleado in listaEmpleComision:
    print(empleado)