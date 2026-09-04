cadena1 = "Hola soy Alan"
cadena2 = "Bienvenido a maquinola"

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("Alan")

#buscamos una cedana en otra cadena, si no hay coincidencias devuelve un error
busqueda_index = cadena1.index("a")


#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias de una cadena dentro de otra cadena , devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("la ma")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("H")

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("n")

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma por el valor 2 
cadena_nueva = cadena1.replace("","")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split


print(termina_con)









#DIR- devuelve una lista con todos los atributos y metodos de un objeto
#UPPER- convierte a mayusculas
#LOWER- convierte a minusculas
#CAPITALIZE- convierte la primera letra en mayuscula
#FIND- busca una cadena en otra cadena, si no hay coincidencias devuelve -1
#INDEX- busca una cadena en otra cadena, si no hay coincidencias devuelve un error
#ISUNUMERIC- devuelve True si todos los caracteres de la cadena son numeros
#ISALPHA- devuelve True si todos los caracteres de la cadena son letras
#COUNT- devuelve el numero de veces que aparece una cadena en otra cadena
#LEN- cuenta los caracteres de una cadena
#ENDSWITH- verifica si una cadena comienza con 
#STARSWITH- verifica si una cadena comienza con 
#REPLACE - remplaza un valor por otro
#SPLIT- separa por el parametro dado





