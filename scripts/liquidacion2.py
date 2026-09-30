"""
CALCULADORA DE LIQUIDACIÓN. Valmos a evaluar lo que sucede cuando despiden a alguien y deben darle, 
además de liquidación normal, una indemnización. A la liquidación, hay que sumarle UN MES de sueldo bruto 
por año trabajado ( a partir del año de antiguedad, cuenta como 1 año más si se superan los 3 meses).
Es decir, si trabajas 1 año y 4 meses, cuenta como dos años, por lo tanto 2 sueldos brutos. Si trabajas 
2 años y 6 meses, cuenta como 3 años... y asi.
Por lo tanto calculemos la indemnización. Para eso necesitamos cantidad de años trababajando de la persona.
Sé original y piensa como puedes pedirle  la antigüedad para luego evaluar su indemnizacion,
teniendo en cuenta esto de los 3 meses.

"""

# input
# salario_bruto = 20000

salario_bruto = int(input("Ingrese su salario bruto: "))
dias_trabajados = int(input("Ingrese los dias trabajados en el último mes: "))
años_antiguedad = int(input("Ingrese los años trabajados: "))
meses_antiguedad = int(input("Ingrese los meses trabajados en el ultimo año: "))
total_antiguedad = años_antiguedad


# calculos

resultado_1 = salario_bruto / 30
liquidacion = resultado_1 * dias_trabajados

if años_antiguedad > 1 and meses_antiguedad > 3:
    indemnizacion= salario_bruto*(años_antiguedad+1)
elif años_antiguedad >= 1 and meses_antiguedad<3:
    indemnizacion = salario_bruto*años_antiguedad
else:
    indemnizacion = 0
    print("No hay indemnizacion.")


#output
print("La liquidación es: $"+str(liquidacion))
print(f"La indemnizacion es de: ${indemnizacion}")

print(f"El total a percibir es de: ${liquidacion+indemnizacion}")





