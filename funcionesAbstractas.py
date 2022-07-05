def completo (nombre, apellido, inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'
    
print(completo ('xavier', 'castillo'))
print(completo('castillo', 'xavier', inverso= True))
print(completo(apellido='castillo', nombre= 'xavier'))