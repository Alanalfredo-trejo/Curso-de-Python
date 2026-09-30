potencial_reposo = -60
umbral_exitacion = range(-55,-49)
mV = int(input("Ingrese los mV a ejecutar en la neurona: "))

resultado = potencial_reposo+mV
print(f"La neurona ahora tiene un potencial de {resultado}mV")

if resultado in umbral_exitacion or resultado > (-50):
    print("Neurona exitada")
else:
    print("No ha pasado nada")

