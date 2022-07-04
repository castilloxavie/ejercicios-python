#funciones decoradores: son funciones q añaden funcionamiento a otras funciones
# la funcion decoradora de estructura en 3  funciones (a,b,c)
#(a)recibe como parametro a (b) para devolver (c)

def funcion_decoradora_a(funcion_parametro_b):
    def funcion_interior_c():
        #acciones adicionales q decoran 
        print("vamos a realizar una operacion matematica")
        funcion_parametro_b()
        
        #mas acciones q decoran
        print("has realizado ya la operacion matemarica")
    return funcion_interior_c


@funcion_decoradora_a # sl metodo (@) sirve para anclar una funcion  decoradora a  otra funcion
def suma():
    print(12+20)

@funcion_decoradora_a    
def resta():
    print(5-2)
    
suma()
resta()