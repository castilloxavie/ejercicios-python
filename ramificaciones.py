nombre=input("ingrese tu nombre: ")
edad=int(input("escriba tu edad: "))

nombre2=input("igrese ingrese otro nombre: ")
edad2=int(input("escriba tu edad: "))

if  edad >  edad2:
    print("el usuario con el ", nombre, "y la", edad, " años,  es mayor que el usuario 2 con", nombre2, "y la ", edad2, " años" )
elif  edad2 ==  edad:
    print("tinen la misma", edad, edad2)
else:
    print("el usuarui de mayor edad es: ", edad2,  " años")