"""
IF ANIDADOS

IF condicion:
    if condicion111:
        instrucciones

ELSE:
    instrucciones 

"""

saber_manejar = input("¿Sabes manejar?: ")
dinero = input("¿Tienes dinero?: ")
bicicleta = input("¿Tienes bicicleta?: ")

if saber_manejar == "si":
    print("Puedes ir en auto")
    
if dinero == "si":
    print("Puedes ir en bus")
if bicicleta == "si":
    print("Puedes ir en bicicleta")

print("Puedes ir caminando")
           