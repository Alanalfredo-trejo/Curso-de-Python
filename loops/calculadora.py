#calculadora del 1 al 10
"""
rango = range(1,11)

numero = int(input("¿Qué número quieres multiplicar?: "))

for num in rango:
    print(f"{numero}+{num} ---> {numero*num}")

"""
#calculadora V 2.0
print("------CALCULADORA V2.0------")
numeros_a_multiplicar = range(1,11)
multiplicadores = range(1,11)

for numero in numeros_a_multiplicar:
    #tabla
    print(f"------- TABLA DEL {numero}:")
    for mult in multiplicadores:
        print(f"{numero}*{mult} ---> {numero*mult}")
        
        


    
    