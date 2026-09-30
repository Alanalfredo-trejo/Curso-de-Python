"""
Ejercicio 1: Crear y acceder a un diccionario.
Crea un diccionario que almacene información sobre libros.
Cada clave debe ser el titulo del libro y el valor asociado debe ser el autor.
Luego; accede a la informacion de al menos dos libros utilizando sus titulos.

"""
libros = {
    "Fundacion":"Isaac Asimov",
    "1984":"George Orwell",
    "Cien años de soledad":"Gabriel García Marquez"
}

libro = "Fundación"
libro2 = "1984"
print(f"El autor de {libro} es {libros[libro]}")
print(f"El autor de {libro} es {libros[libro2]}")

libros2 = [["Fundacion","Isaac Asimov"],"1984","Cien años de soledad2"]
libros["Los juegos del hambre"] = "Suzanne Collins"

print(libros)

for titulo,autor in libros.items():
    print(f"El autor de {titulo} es {autor}")
    
    
    
