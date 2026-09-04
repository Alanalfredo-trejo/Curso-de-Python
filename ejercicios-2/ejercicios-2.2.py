#creando una funcion que nos devuelva los numeros primos
#entre 0 y el argumento que pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse
    #por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina en bucle
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3,num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos 
resultado = primos_hasta(98)
print(resultado)


        
