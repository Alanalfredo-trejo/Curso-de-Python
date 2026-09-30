lista_peliculas = ["Matrix","Interestellar","El origen","Chihiro"]
print(lista_peliculas)

#Recorrer mi lista con FOR
for pelicula in lista_peliculas:
    print(pelicula)

print(lista_peliculas[1])

lista_peliculas[2] = "Otra pelicula"
print(lista_peliculas)

#slicing
print(lista_peliculas[:3])

#Sumarlas e Igualarlas
lista_peliculas2 = ["Matrix","Interestellar","El origen","Chihiro","Yo robot"]
if lista_peliculas != lista_peliculas2:
    lista_peliculas3 = lista_peliculas + lista_peliculas2
    print(lista_peliculas)

lista_2 = [["Tatiana","Pepita","Rosita"],"Hola",["Bananas","Manzana"]]
print(lista_2)




