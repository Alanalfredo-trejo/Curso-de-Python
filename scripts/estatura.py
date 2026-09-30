estatura = int(input("¿Cual es tu estatura?: "))

# chequeos 
if estatura <= 150:
    print("Persona de baja estatura")
elif estatura <=170 and estatura >150:
    print("Persona de media estatura")
elif estatura >170:
    print("Persona de alta estatura")

