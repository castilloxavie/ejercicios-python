# el guardado permanente en ficheros externos para guardar paulatinamente de diversos programasRamificados
import pickle

class persona:
    def __init__(self,nombre, genero, edad):
        self.nombre=nombre
        self.genero= genero
        self.edad= edad
        print("se ha creado una persona nueva con nombre de ", self.nombre)
        
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad )

class listaPersona:
    personas=[]
    
    # crear constructor 
    def __init__(self):
        listaDePersonas=open("ficheroExterno", "ab+") # la (ab+) es agregar informacion.
        listaDePersonas.seek(0)
        try:
            self.personas=pickle.load(listaDePersonas)
            print("se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("el fichero esta vacio")
        finally:
            listaDePersonas.close()
            del (listaDePersonas)
    
    def agregarPersona(self,p):
        self.personas.append(p) # esta funcion lo q hace es agregar a la lista nueva informacion
        self.guardarPersonasFicheroExterno()
        
    def mostrarPersona(self):
        for p in self.personas:
            print(p)
            
    def guardarPersonasFicheroExterno(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)
        
    def mostrarInfoFicheroExterno(self):
        print("la informacion del fichero es la siguiente")
        for p in self.personas:
            print(p)

miLIsta=listaPersona()      
pers=persona("ama"," femenina", 230 )
miLIsta.agregarPersona(persona)
miLIsta.mostrarInfoFicheroExterno()