mi_diccionario = {
    "nombre":"Tatiana",
    "edad":25,
    "apellido":"Sorroche",
    "profesion":"Software Enginer",
    "peliculas":["Matrix","Interestellar","Chihiro"],
    "Informacion_canal":{"nombre":"1lugarparapensar","suscriptores":18000}
}

#metodos
#devuelve keys
print(mi_diccionario.keys())
del mi_diccionario["peliculas"]
print(mi_diccionario.keys())

#devuelve values
print(mi_diccionario.values())

print(dir(mi_diccionario))

dicc2 = {
    "movies":{
        "pelicula1": {
            "nombre":"matrix",
            "año":1998
            
        },
        "pelicula2": {
            "nombre":"Interestellar",
            "año":2019
        }       
    },
    "series":{
        "serie1":{
            "nombre":"gossipgirl",
            "año":2010
        }
    }
}

print(dicc2["movies"]["pelicula2"]["nombre"])
print(dicc2["movies"]["pelicula1"].keys())

