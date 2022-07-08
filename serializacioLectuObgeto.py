import pickle

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
        print("marca: ", self.marca, "modelo: ", self.modelo, "en marcha: ", self.marcha, "acelerado ", self.acelera, "frenado: ", self.fena)
        
fifcheroApertura=open("los coches", "rb")
miscohess=pickle.load(fifcheroApertura)
fifcheroApertura. close()

for c in miscohess:
    print(c. estado())