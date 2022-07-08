"""en es te ejerciico ser ara aproximaciones a la 
   laiz cuadeada e en la q vamos a trabajar a continiacion
"""

inicio= int(input("indique su numero a verificar su aproximacion: "))
oproximacion = 0.01
paso = oproximacion **2
respuesta= 0.0

while  abs (respuesta ** 2 -inicio) >= oproximacion and respuesta - inicio:
    print(abs(respuesta** 2))
    respuesta += paso
    
if abs (respuesta ** 2 - inicio) >= oproximacion:
    print(f'no se encuentra una proximacion a la raiz cuadrada de {inicio}')
else:
    print(f'la raiz cuadrada de {inicio} es {respuesta}')