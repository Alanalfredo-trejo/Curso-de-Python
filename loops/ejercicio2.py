"""
-Seguir una receta para hacer galletas de chocolate. Hay que poner 100ml de leche, 30gr de harina y 10 gramos de chocolate.
Ayudarse del while para hacer eso. En caso de que el usuario se pase con los ingredientes, tirarlos y volver a cero.

-Input:
Harina
leche
chocolate

-Camino:
Pedirle al usuario los ingredientes hasta que se lluegue a lo correcto, si se pasa de alguno debe 
empezar de nuevo.

-Output:
100 de leche 
30 de harina
10 chocolate

"""
leche = 0
harina = 0 
chocolate = 0

while leche < 100 or harina <30 or chocolate < 10:
    leche += int(input("ML de leche a agregar: "))
    harina += int(input("Gr de harina a agregar: "))
    chocolate += int(input("Gr de chocolate a agregar: "))
    
    if leche >100 or harina > 30 or chocolate > 10:
        #resetear todas las variables
        print("Te excediste con los ingredientes, empieza de nuevo.")
        leche = 0
        harina = 0
        chocolate = 0

print("Felicidades, puedes comer tus galletas en 30 min.")


 

