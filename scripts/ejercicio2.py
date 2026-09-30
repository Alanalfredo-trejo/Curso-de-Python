#Preguntar al usuario
nombre = input("¿Cual es tu nombre?: ")
edad = input("¿Cual es tu edad: ")
direccion = input("¿Cual es tu direccion: ")
telefono = input("Cual es tu numero de telefono: ")

#Almacenar toda la info en un diccionario
usuario = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}

#Imprimir la informacion accediendo a los valores del diccionario
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su numero de telefono es {usuario['telefono']}")
