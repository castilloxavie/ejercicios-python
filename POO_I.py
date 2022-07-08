# las clases son las partes q forman un obgeto. tienen un estado, un corpontamiento y unas propiedades
class coche():
    
    def __init__(self):#constructor de las clases
        self.__lagoChasis= 200 #encapsulamiento (__) esto permite que nadie desde afuera pueda mudificar los datos de la clase
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    #comportamiento o metodos
    def arracar(self,arrancamos): # funcion de metodos  es diferente a las otras funciones ya q estas funciones estan dentro de una clase.
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
            
        
        if(self.__enmarcha and chequeo):
                       return "el coche esta enmarcha"

        elif(self.__enmarcha and chequeo=="false"):
            return "algo esta mal en el chequeo del auto"
        else:
            return "el coche esta parado"
     
       
        
    def estado (self):
        print("el coche tiene ", self.__ruedas, " ruedas. un ancho de ", self.__anchoChasis, 
              " cm y un largo ",self.__lagoChasis, " cm")
        
    
    def __chequeo_interno(self):
        print("realizar chequeo")
        self.gasolina="ok"    
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas" ):
            return True
        else:
            return False
#obgeto,  instancia de clase y ejemplar de clase
micoche=coche()
print(micoche.arracar(True)) 
micoche.estado()

print("---------------------a continuacion creamos el segundo objeto--------------------")

miAuto= coche()
print(miAuto.arracar(False))   
miAuto.estado()  
    