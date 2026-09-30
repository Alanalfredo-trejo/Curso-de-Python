lista_peliculas = ["Matrix","Interestellar","El origen","Chihiro","Yo robot"]

#Metodos listas
#append : agregar elementos a mi lista
lista_peliculas.append("Totoro")

#insert : insertar un elemento en un indice especifico
lista_peliculas.insert(3,"Castillo vagabundo")

#eliminar un elemento
# posicion : 
lista_peliculas.pop(0)
#nombre -> da error si no encuentra el elemento en la lista
lista_peliculas.remove("Interestellar")

#len : longitud
print(len(lista_peliculas))

#ordenar una lista de mayor a menor o alfabeticamente
print(lista_peliculas.sort())

#ordenar de manera inversa: revertir mi lista
print(lista_peliculas.reverse)

