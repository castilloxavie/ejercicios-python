#herencia  en programacion es basicamente ver q caracteristicas tienene en similar los objetos y comportamientos.
class vehiculos(): # clase padre
    def __init__(self, marca, modelo): #constructor (__init__)
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.fena=False
        
    #metodos
    def arracar(self):
        self.enmarcha=True
        
    def acelerar(self):
        self.acelera=True
        
    def frenar(self):
        self.fena=True
        
    def estado(self):
        print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nenmarcha: ", self.enmarcha, 
              "\nacelerado: ", self.acelera, "\nfrenado: ", self.fena) # el salto de linea ("\n")

class furgoneta(vehiculos):
    def carga (self, cargar): 
        self.cargado=cargar
        if(self.cargado): 
            return "la furgoneta esta cargada"
        else:
            "la furgoneta esta vacia"    
        
class moto(vehiculos):# aca se pueden agregar caracteristicas propias q son muy diferente a lo q puede compartir con los otros vehiculos deacuerdo al ejerccio en desarrollo
    hcaballito=""
    def picada(self):
        self.hcaballito="voy haciendo piruetas"
        
    #sobreescribir simplemente es colocar el metodo q necesitamos  dentro de la clase hijo y agregar esas caracteristicas q en especial hace ese objeto
        def estado(self):
            print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nenmarcha: ", self.enmarcha, 
              "\nacelerado: ", self.acelera, "\nfrenado: ", self.fena, "\npica la toto: ", self.hcaballito) # el salto de linea ("\n")

class vehiculo_electrico(vehiculos):# esta es una clase independiente no hereda nada de laclase padre.
    def __init__(self, marca, modelo):
        
        super().__init__(marca,modelo )
        
        self.autonomia=100
        
    def caragarenergia(self):
        self.cargando=True
       

miMoto=moto("honda", "cbr")
miMoto.picada()
miMoto.estado() #objeto de la clase

miFurgineta=furgoneta("chevrolet", "king")
miFurgineta.arracar()
miFurgineta.estado()
print(miFurgineta.carga(True))

class bicicletaElectrica(vehiculo_electrico, vehiculos): # la union de dos clases se conoce como herencia multiple
    pass
mibice=bicicletaElectrica("jak", "king")
     