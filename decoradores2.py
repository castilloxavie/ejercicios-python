#decoradores con parametros
def funcion_decoradora_a(funcion_parametro_b):
    def funcion_interior_c(*args, **kwargs): # el metodo (*args)sirve para decir q va a resivir un numero indeterminado de parametros, el metodo (**kwargs) sirve cuando lleva una clave y un valor la operciona realizar
        #acciones adicionales q decoran 
        print("vamos a realizar una operacion matematica")
        funcion_parametro_b(*args, **kwargs)
        
        #mas acciones q decoran
        print("has realizado ya la operacion matematica")
    return funcion_interior_c


@funcion_decoradora_a # sl metodo (@) sirve para anclar una funcion  decoradora a  otra funcion
def suma(num, num1,num2):
    print(num+num1+num2)

@funcion_decoradora_a    
def resta(num, num1):
    print(num-num1)
    
@funcion_decoradora_a
def potencia(base,exponente):
    print(pow(base,exponente))
    
suma(50, 50, 70)
resta(17,38)
potencia(base=10,exponente=3)