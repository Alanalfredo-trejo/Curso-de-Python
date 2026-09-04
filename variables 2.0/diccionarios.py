#creando diccionarios con dict ()
diccionario = dict(nombre="lucas",apellido="dalto")

#las listas pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio"]):"jajaja"}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido"],"No sé")

print(diccionario["nombre"])
