#muchas formas es lo q quiere de cir polimorfirmos
class coche():
    
    def desplazamiento(self):
        print("me desplazo utilizando 4 ruedas")
        
class moto():
    def desplazamiento (self):
        print("me desplazo urilizando 2 ruedas")
        
class camion ():
    def desplazamiento(self):
        print("me desplazo utilizando 6 ruedas")
            
# aca entra el polimorfirmos
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
mivehiculo=camion()
desplazamientoVehiculo(mivehiculo)

mivehiculo=moto()
desplazamientoVehiculo(mivehiculo)

mivehiculo=coche()
desplazamientoVehiculo(mivehiculo)