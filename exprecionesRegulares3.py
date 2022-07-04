import re
listas_nombre=[
     "ana",
     "pedro",
     "maria",
     "rosa",
     "sandra",
     "celia"
]

for elemntos in listas_nombre:
    if re.findall("[o-t]", elemntos): # en los metacaracteres tambien se hacen rangos cono se explrea en el ejemplo 
        print(elemntos)
        
lista_ciudades=[
   "ma1",
   "se1",
   "ma2",
   "ba1",
   "ma3",
   "va1",
   "va2",
   "ma4",
   "maA",
   "ma5",
   "maB",
   "maC"
]

for ii in lista_ciudades:
    if re.findall("ma[0-3]", ii): # mostrar el rango
        print(ii)
        
for ix in lista_ciudades:
    if re.findall("ma[^0-3]", ix): #mostrar algo diferente  de lo q esta entre el rango de parametro en el ejemplo
        print(ix)
        
for xa in lista_ciudades:
    if re.findall("ma[0-3A-B]", xa):
        print(xa)