#Reto: Escribe un script que solicite al usuario su edad con input() (recuerda que input() siempre devuelve un string,
#por lo que debes convertirlo a entero con int()) y determine la categoría:

#Menor de 13: "Infantil"

#De 13 a 17: "Adolescente"

#De 18 a 64: "Adulto"

#65 o más: "Adulto Mayor"

#Lo que aprendes: Entradas de usuario (input), conversión de tipos (int()), condicionales (if, elif, else)
# e impresión formateada con f-strings (print(f"Tienes {edad} años")).

input_edad = input("Por favor, ingresa tu edad:")
edad = int(input_edad)
if edad < 13:
    print("Infantil")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 64:
    print("Adulto")
else:
    print("Adulto Mayor")

print(f"Tienes {edad} años")

    