"""
Escribe un programa que pida al usuario que ingrese un número.
Chequear si el número ingresado es par o impar.
Imprimir por pantalla si es par o impar.

"""

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("El número {} es PAR".format(numero))
else:
    print("El número es IMPAR".format(numero))



