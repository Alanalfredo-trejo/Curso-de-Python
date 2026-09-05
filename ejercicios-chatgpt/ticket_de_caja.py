producto = "Audifonos"
precio_unitario = 50.00
cantidad = 26
descuento = False

subtotal = precio_unitario * cantidad
if descuento:
    total_final = subtotal -(subtotal * 0.10) # o tambien puede ser subtotal * 0.90
else:
    total_final = subtotal

print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: {subtotal}")
print(f"Descuento: {subtotal * 0.10 if descuento else 0}")
print(f"Total final: {total_final}")

