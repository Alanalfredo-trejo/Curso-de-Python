#SINTAXIS
mi_diccionario = {
    "nombre":"Tatiana",
    "edad":25,
    "apellido":"Sorroche",
    "profesion":"Software Enginer"
}

print(mi_diccionario["nombre"])
print(mi_diccionario["profesion"])

#cumpleaños
mi_diccionario["edad"] += 1
print(mi_diccionario["edad"])

for k in mi_diccionario:
    print(k)
    print(mi_diccionario[k])


