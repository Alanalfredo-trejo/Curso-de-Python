inventario = [
    {"nombre": "Teclado", "precio": 45.0, "stock": 10},
    {"nombre": "Monitor", "precio": 180.0, "stock": 4},
    {"nombre": "Mousepad", "precio": 15.0, "stock": 25},
    {"nombre": "Cámara web", "precio": 65.0, "stock": 8},    
]

total_valor_premium = 0.0
for producto in inventario :
    if producto["precio"] > 50.0:
        total_valor_premium += producto["precio"] * producto["stock"]
        print(f"Producto premium: {producto['nombre']} - Precio: {producto['precio']} - Stock: {producto['stock']}")

print(f"El valor total de los productos premium es: {total_valor_premium}")
