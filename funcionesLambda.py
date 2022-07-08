# las funciones (lambda)son funciones anoninas
"""def area_triangulo(base, altura): # funcion normal
    return(base*altura/2)

triangulo1=area_triangulo(6,4)
triangulo2=area_triangulo(2,5)
triangulo3=area_triangulo(56,89)

print(triangulo1)
print(triangulo2)
print(triangulo3)"""

#-------------------funciones lambda----------------------
area_triangulo=lambda base,altura:(base*altura)/2
print(area_triangulo(2,69))
print(area_triangulo(23,45))

print("potencias")
alCubo=lambda numero:pow(numero,3) # el metodo (puow)sirve para exponentes
print(alCubo(23))

print("ejemplos")
altcubo=lambda numero:numero**3
print(altcubo(6))

print(" otros ejemplos")
destacar_comision=lambda comisio:"$¡{}!".format(comisio)

comisio_ana=20000
print(destacar_comision(comisio_ana))

# las funciones lambda principalmente sirve para realizar funciones simples q no contengan un grado de complejidad en su funcionalidad.