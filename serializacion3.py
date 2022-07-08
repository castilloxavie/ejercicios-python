import pickle
# crear un codigo binario de un obgeto

class ve():
    def __init__(self, marca,modelo):
        self.marca=marca
        self.modelo = modelo
        self.marcha=False
        self.acelera=False
        self.fena=False
        
    def arrancar(self):
        self.acelera=True
        
    def acelerar(self):
        self.acelera=True
        
    def frenar(self):
        self.fena=True
        
    def estado(self):
        print("nraca: ", self.marca, "modelo: ", self.modelo, "en marcha: ", self.marcha, "acelerado ", self.acelera, "frenado: ", self.fena)
        
coche1= ve("mazda", "mx5")
coche2= ve("seat", "leon")
coche3= ve("renault", "megane")

coches=[coche1, coche2, coche3]

fifchero=open("los coches", "wb")
pickle  .dump(coches, fifchero)
fifchero.close()
del (fifchero)

