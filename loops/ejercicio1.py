"""
Escriba un programa que pregunte cúantos números se van a introducir, pida estos números, y diga al
final cuántos han sido pares y cúantos impares.

# INPUT
-cuantos numeros a chequear
-números en si a chequear

#CAMINO
-mientras no haya llegado a la cantidad de números a chequear
-pedir al usuario número a chequear
-hacer chequeo

#OUTPUT
-cuántos números son pares
-cuántos números son impares
"""

numeros_a_chequear = int(input("¿Cuántos números vas a ingresar?: "))

contador_numeros = 0
contador_impar = 0
contador_par = 0

while contador_numeros < numeros_a_chequear:
    numero =int(input("Ingrese un número: "))
    #chequeo  si es par o impar
    if numero % 2 == 0:
        print(f"{numero} es un numero par")
        contador_par +=1
    else:
        print (f"{numero} es un numero impar")
        contador_impar +=1
    
    contador_numeros +=1
    
    print(f"El total de numeros pares ha sido: {contador_par}")
    print(f"El total de numeros impares ha sido: {contador_impar}")
    
    
    


