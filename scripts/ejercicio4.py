usuarios = {}

while True:
    print("Que quieres hacer?")
    print("1.Agregar una persona")
    print("2. Buscar una persona")
    print("3. Salir")
    
    opcion = int(input("Opcion"))
    
    if opcion == 1:
        #Preguntar al usuario
        nombre = input("¿Cual es tu nombre?: ")
        edad = input("¿Cual es tu edad: ")
        direccion = input("¿Cual es tu direccion: ")
        telefono = input("Cual es tu numero de telefono: ")

        #Almacenar toda la info en un diccionario
        usuarios [nombre] = {
            "nombre": nombre,
            "edad": edad,
            "direccion": direccion,
            "telefono": telefono
        }
        
    elif opcion == 2:
        nombre = input("¿Cual es el nombre que quieres buscar?: ")
        if nombre in usuarios:
             print(f"{nombre} tiene {usuarios[nombre]['edad']} años, vive en {usuarios[nombre]['direccion']} y su numero es {usuarios[nombre]['telefono']}")
        else:
            print("No existe la persona en los datos")
    elif opcion == 3 :
        break
    
    else:
        print("La opción no está disponible.")
    
                         
                             