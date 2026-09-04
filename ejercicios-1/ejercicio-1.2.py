#le pedimos al usuario que nos diga una frase o varias
# --- 1. ENTRADA DE DATOS ---
# input() detiene el programa para que el usuario escriba su frase en la consola.
# El texto ingresado se guarda como una cadena de texto (string) en la variable 'frase'.
frase = input("decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

#creamos una lista con todas las palabras de la frase ( se deparan cada vez que haya un espacio en blanco)
# --- 2. PROCESAMIENTO DE LA FRASE ---
# .split(" ") corta el texto cada vez que encuentra un espacio en blanco
# y convierte la frase en una lista de palabras individuales.
palabras_separadas = frase.split(" ") 

#usamos len ( para ver la cantidad de elementos que hay en la lista)
# len() cuenta cuántos elementos (palabras) tiene la lista resultante.
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de un minuto al decirlo, le decimos que pare un poco
# --- 3. VALIDACIÓN (CONDICIONAL) ---
# Asumiendo una velocidad promedio de 2 palabras por segundo, 120 palabras tomarían 60 segundos (1 minuto).
# Si la frase excede las 120 palabras, envía una advertencia humorística.
if cantidad_de_palabras > 120: 
    print ("para flaco tampoco te pedi un testamento")

#calculamos cuanto tardaria en decir las palabras y se lo decimos

print(f'Dijiste{cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
# Calcula el tiempo de Alan considerando que habla un 30% más lento (factor de 1.3):
# Usa el truco de multiplicar por 100 y usar la división entera (//) para limitar los decimales.
print(f'Alan lo daria en {cantidad_de_palabras * 100 // 2 *1.3 / 100} segundos')
