#El Problema: Calculadora de Propina y Descuento en un Restaurante Vas a calcular cuánto debe pagar cada persona en un grupo al salir a comer,
#dependiendo de si son muchas personas (aplicando un pequeño cargo o aviso) y considerando que un miembro del grupo ("Alan") siempre consume un poco más.

#1.-Entrada de datos: Pide al usuario que ingrese el total de la cuenta en pesos.

#2.-Entrada de datos: Pide cuántas personas hay en la mesa.

#3.-Condicional: Si son más de 8 personas, muestra un mensaje en pantalla que diga: "¡Grupo grande! Se incluirá servicio mesa."

#.-Cálculos:

#Calcula cuánto pagaría cada persona en partes iguales (dividiendo el total entre el número de personas).

#Calcula cuánto pagaría Alan, asumiendo que él consume un 20% más que el promedio (multiplica el pago promedio por 1.2).

#Salida de datos: Muestra en pantalla ambos resultados en un mensaje claro.

total_cuenta = float(input("ingrese el total de la cuenta ($): "))
cantidad_personas = int(input("¿Cuantas personas van a pagar?: "))

if cantidad_personas > 8:
    print("Grupo grande! Se incluira servicio de mesa especial.")
    
pago_promedio = total_cuenta / cantidad_personas
pago_alan = pago_promedio * 1.20 

print (f'Cada persona debe pagar : ${pago_promedio}')
print(f'Alan debe pagar: ${pago_alan} (por que consumió un 20% más)')


