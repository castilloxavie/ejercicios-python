from setuptools import setup # esto se hace para hacer un paquete distribuible.

setup(
    name="paquete", 
    version="1.0",
    description="paquete de redondeo y potencia",
    author="xavier",
    author_email="xavieralbertocastillovaron@hotmail.com",
    packages=["PAQUETES", "PAQUETES.redondear_potencia"]
    
)
#debemos de tener en cuenta q esto nos sirve para instalarlo al sistema operativo de tu pc para 
#cuando estas en cualquierparte de tu codigo pueda funcionar esto nos dice q no importa si usted mueve el archivo a otra direccion siempre se va a poder ejecutar.
