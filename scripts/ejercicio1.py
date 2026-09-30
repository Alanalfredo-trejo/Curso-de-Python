"""
Escribir un programa que guarde una variable el diccionario {'Euro','Dollar','Yen'},
pregunte al usuario por una divisa y muestre du dimbolo o un mensaje de aviso si la divisa no está en el diccionario.

"""

divisas = {'Euro':'e','Dollar':'D','Yen':'Y'}
divisa = input("Ingrese la divisa que quiere consultar: ").title()

if divisas.get(divisa):
    simbolo = divisas[divisa]
    print(f"El simbolo de la divisa {divisa} es : {simbolo}")
else:
    print('La divisa no existe')

"""
try:
    simbolo = divisas[divisa]
    print(f"El simbolo de la divisa {divisa} es: {simbolo})
except KeyError:
    print('La divisa no existe')

"""

