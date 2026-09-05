# Función 1: Recibe un monto y retorna el 16% de IVA
def calcular_iva(monto):
    return monto * 0.16

# Función 2: Procesa la compra aplicando descuento e IVA
def procesar_compra(precio_base, porcentaje_descuento=0):
    # Corrección: dividimos entre 100 para convertir el entero a porcentaje decimal
    monto_descuento = precio_base * (porcentaje_descuento / 100)
    monto_con_descuento = precio_base - monto_descuento
    iva = calcular_iva(monto_con_descuento)
    
    total_a_pagar = monto_con_descuento + iva
    return total_a_pagar, monto_descuento, iva


# --- PRUEBAS DE INVOCACIÓN ---

# Prueba 1: Producto de $100 con 10% de descuento
# Desempaquetamos la tupla que retorna la función directamente en 3 variables:
total1, descuento1, iva1 = procesar_compra(100.0, 10)
print(f"Compra 1 -> Total: ${total1} | Descuento: ${descuento1} | IVA: ${iva1}")

# Prueba 2: Producto de $200 sin especificar descuento (usa el valor por defecto: 0)
total2, descuento2, iva2 = procesar_compra(200.0)
print(f"Compra 2 -> Total: ${total2} | Descuento: ${descuento2} | IVA: ${iva2}")


    