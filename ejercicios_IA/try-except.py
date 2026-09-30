def procesar_edades (lista):
    edades_validas = []
    for edad in lista:
        try:
            edad_int = int(edad)
            if edad_int < 0:
                raise ValueError("La edad no puede ser negativa.")
            edades_validas.append(edad_int)
        except ValueError as e:
            print(f"Error al procesar la edad '{edad}': {e}")

    print(f"Edades válidas: {edades_validas}")
    return edades_validas

procesar_edades(["25", "treinta", "-5", "40", "abc"])

    
def procesar_edades(lista):
    # "lista" es el parámetro: aquí vas a recibir la lista de edades
    # que quieras revisar cuando llames a la función.

    edades_validas = []
    # Creamos una lista vacía. Aquí vamos a ir guardando
    # solo las edades que SÍ sean correctas (números positivos).

    for edad in lista:
        # Este bucle "for" recorre uno por uno los elementos de la lista.
        # En cada vuelta, la variable "edad" toma el valor de un elemento.
        # Ejemplo: primera vuelta edad = "25", segunda vuelta edad = "treinta", etc.

        try:
            # "try" significa "intenta hacer esto".
            # Si algo sale mal dentro de este bloque, Python no se detiene,
            # sino que salta directo al "except" de abajo.

            edad_int = int(edad)
            # Aquí intentamos convertir el texto (string) a número entero.
            # Si "edad" es algo como "25", esto funciona sin problema.
            # Pero si "edad" es "treinta" o "abc", Python NO puede convertirlo
            # y lanza un error automáticamente (ValueError).

            if edad_int < 0:
                # Si la conversión sí funcionó, revisamos si el número es negativo.
                raise ValueError("La edad no puede ser negativa.")
                # "raise" significa "yo mismo voy a generar un error a propósito".
                # Aunque Python no vea nada "roto" aquí (el número sí se convirtió bien),
                # TÚ decides que una edad negativa no tiene sentido,
                # así que fuerzas un error con tu propio mensaje.

            edades_validas.append(edad_int)
            # Si todo salió bien (se convirtió y no es negativo),
            # agregamos el número a nuestra lista de edades válidas.

        except ValueError as e:
            # "except" significa "si algo falló arriba, haz esto en su lugar".
            # ValueError es el TIPO de error que estamos esperando capturar.
            # "as e" guarda el mensaje del error dentro de la variable "e",
            # para que podamos usarlo después (por ejemplo, para imprimirlo).

            print(f"Error al procesar la edad '{edad}': {e}")
            # Mostramos en pantalla cuál edad falló y por qué.
            # El programa NO se detiene aquí, sigue con la siguiente vuelta del "for".

    print(f"Edades válidas: {edades_validas}")
    # Ya que terminó de revisar TODAS las edades de la lista,
    # imprimimos cuáles pasaron la prueba.
    return edades_validas