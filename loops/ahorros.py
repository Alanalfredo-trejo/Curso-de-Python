"""
Yo quiero ahorrar dinero
El programa me va a preguntar cuanto quiero ahorrar
Y luego me va a preguntar cuanto ahorro hasta que llegue al objetivo

"""
objetivo = float(input("¿Cuanto dinero quieres ahorrar): "))
ahorrado = 0
fin = False

while ahorrado < objetivo and fin != True:
    cantidad_a_agregar = float(input("Indica cuantos euros quieres guardar: "))
    ahorrado += cantidad_a_agregar
    if cantidad_a_agregar == 11:
        fin = True
        
print("Has llegado a tu objetivo! FELICITACIONES!")


      
