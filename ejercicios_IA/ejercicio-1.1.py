input_calificacion = input("Por favor, ingresa tu calificación:")
calificacion = float(input_calificacion)
if calificacion < 5:
    print("Reprobado")
elif 5 <= calificacion < 7:
    print("Aprobado")
else:
    print("Sobresaliente")

print(f"Tu calificación es: {calificacion}")
print(f"Tu calificación es: {calificacion:.2f}")
print("Evaluación completada.")

