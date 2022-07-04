#herencia (super()) esta palabra reservada lo q nos hace es q llama tol de la clase padre de manera primaria
class persona():
    def __init__(self, nombre, edad, recidencia):
        self.nombre=nombre
        self.edad=edad
        self.recidencia=recidencia
        
    def descriccion(self):
        print("nombre: ", self.nombre, "\nedad: ", self.edad, "\nrecidencia: ", self.recidencia)
        
        
class empleado(persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
        
    def descriccion(self):
        super().descriccion()
        print("salari: ", self.salario, "\nantiguedad: ", self.antiguedad, "años")
        
#instacio de clase o objeto
nom=empleado(2000, 15, "xavier", 28, "hogares soacha")
nom.descriccion()
print(isinstance(nom, empleado))# la palabra reservada (isinstance) nos sirve para mirar siertas cosas si son de la clase o no.

