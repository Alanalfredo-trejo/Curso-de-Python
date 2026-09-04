#creando un conjunto con set

conjunto = set(["Dato1","Dato2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato 3"}

print(conjunto2)

#Teoria de conjuntos
conjunto1 = {conjunto2.issubset(conjunto1)}
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

print(resultado)


