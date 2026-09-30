# operadores de comparación
# condicionales 

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print(f"{numero1} es mayor a {numero2}")
elif numero1 == numero2:
    print("Los números son iguales")
else: 
    print(f"{numero2} es mayor a {numero1}")
