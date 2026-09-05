numeros = [3,8,12,5,7,20,14,1,6,9]
suma_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        suma_pares += numero
        print(f"El número {numero} es par")

print(f"La suma de los números pares es: {suma_pares}")



