"""
Realiza un programa que pida al usuario que ingrese su edad y su nacionalidad. Realizar los siguientes chequeos.
-Si tiene 18 o más años, es mayor de edad y es obligatorio votar.
-Si tiene 16 o 17 años, no es mayor de edad pero es opcional votar.
-Si tiene menos de 16 años, no puede votar.
-Si es Mexicano puede votar
-Si no es Mexicano pero tiene ciudadania, puede votar.
-Si no es Mexicano y no tiene ciudadania, no puede votar.
Tener en cuenta ambas condiciones, nacionalidad y edad, para determinar si la persona puede votar o no.
El programa debe indicar, según la edad y la nacionalidad, si la persona puede votar o no.

"""
edad = int(input("Ingrese su edad: "))
pais = input("¿Es usted Mexicano o tiene ciudadania Mexicana?: ")

if edad >18 and pais == "si":
    print("Te es obligatorio votar")
elif edad >= 16 and edad < 18 and pais == "si":
    print("Puedes votar, pero no es ibligatorio")
elif edad < 16 and pais == "si":
    print("No puedes votar por que eres menor de edad.")
else:
    print("No puedes votar porque no eres Mexicano. ")

