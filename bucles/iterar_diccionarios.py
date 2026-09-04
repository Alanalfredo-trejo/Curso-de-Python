diccionario = {
    "nombre": "Alan",
    "apellido": "Trejo",
    "subs": 1000000    
}

#recorriendo diccionario para obtener las claves
for key in diccionario:
    key
    print("la clave es: {key}")



for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")
    