#elementos con subelementospara eso sirve yield from
print("llamar ciudades")

def devuelve_ciudades(*ciudades):
    for elementos in ciudades:
        #for subelemento in elementos:
            yield  from elementos
        
ciudades_devueltas=devuelve_ciudades("colombi","brasil", "ecuador")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
    