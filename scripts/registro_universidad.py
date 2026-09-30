"""
Registrarse en universidad. Realizar un programa que le pida al usuario que ingrese su edad (recordar
el comando input y que siempre es un string), en el caso de que su edad sea menos a 18 o mayor a 80,
imprimir que no puede registrarse en la universidad, caso contrario, imprimir que si puede registrarse.

"""
# Input

try:
    print("Bienvenido a Universidad Pensar")
    edad = int(input("Ingrese su edad: "))

    if edad >= 18 and edad < 80:
        estudios_secundarios = input("¿Terminó sus estudios secundarios? Responda si|no: ")
        if estudios_secundarios == "si" or estudios_secundarios == "SI" or estudios_secundarios == "Si":
            print("Enhorabuena! Puedes inscribirte en la universidad")
        elif estudios_secundarios == "no" or estudios_secundarios == "NO" or estudios_secundarios == "No":
            print("Lo sentimos, no puede registrarse.")
        else:
            print("Lo sentimos! NO puedes inscribirte en la universidad")
    else:
        print("Lo sentimos NO puede registrarse.")
except ValueError:
    print("Ingresa un número valido")

    
    


    
    