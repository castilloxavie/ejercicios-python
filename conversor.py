def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos " + tipo_pesos +"tiene:? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")


menu = """"
bienvenidos al conversor de moneda 💰

1 - pesos colombianos
2 - pesos argentinos 
3 - pesos mexicanos

elija tu opcion 
"""
opcion = int(input(menu))

if opcion == 1:
   conversor("colombiano", 3875)
elif opcion == 2: 
    conversor("argentino", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingrese una opcion correcta")




