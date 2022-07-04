"""""en estas dos funciones tamos busca
el area del cuadrado y 
el area del triangulo. la documentacion
nos sirve para ir trabajando en equipo y tambien cuando se retoma programas  donderdagya se habia dejado de trabajar
y poder saber para q sirve o q hacia el codigo completo o fracmentos del codigo
"""
class areas:
    def areacuadrado(lado):
        """""en estas dos funciones tamos busca
    el area del cuadrado y 
    el area del triangulo. la documentacion
    nos sirve para ir trabajando en equipo y tambien cuando se retoma programas  donderdagya se habia dejado de trabajar
    y poder saber para q sirve o q hacia el codigo completo o fracmentos del codigo
    """
        return "el area del cuadrado es: " + str(lado*lado)

    def area_triangulo(base, altura):
        """""en estas dos funciones tamos busca
    el area del cuadrado y 
    el area del triangulo. la documentacion
    nos sirve para ir trabajando en equipo y tambien cuando se retoma programas  donderdagya se habia dejado de trabajar
    y poder saber para q sirve o q hacia el codigo completo o fracmentos del codigo
    """
        return "el area del triangulo es: " + str((base*altura)/2)
    
help(areas)
print(areas.area_triangulo(2,8))
print(areas.areacuadrado(6))