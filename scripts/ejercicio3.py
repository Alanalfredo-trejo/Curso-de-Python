frutas = {
    "Banana": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

fruta_usuario = input("Ingrese una fruta: ").title()
kg_usuario = float(input("Ingrese los kilos: "))

if kg_usuario <= 0:
    print("Los kilos ingresados deben ser mayores a cero")    
elif fruta_usuario in frutas:
    precio = round(frutas[fruta_usuario] * kg_usuario,2)
    
    print(f"El precio de {kg_usuario} kg de {fruta_usuario} es de: ${precio}")
else:
    print('La fruta no existe')
    