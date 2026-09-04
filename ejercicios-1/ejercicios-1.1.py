#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
alan_curso = 1.5

#Diferencia de duracion 
#--- 2. CÁLCULO DE PORCENTAJES DE AHORRO DE TIEMPO ---
# Fórmula general de porcentaje: (Valor parcial / Valor total) * 100
# Al restar este resultado de 100, obtenemos "cuánto tiempo MÁS RÁPIDO" o "qué porcentaje MENOS" dura el curso de Alan.

# Calculamos qué porcentaje es 1.5 respecto a 2.5 y se lo restamos a 100:

diferencia_con_min_ = 100 - alan_curso / otros_cursos_min * 100   # 100 - 1.5 / 2.5 * 100

# En esta línea se hace un truco para evitar decimales infinitos mediante división entera (//):
# 1. Multiplica 1.5 * 1000 (= 1500)
# 2. Hace división entera entre 4 (= 375)
# 3. Divide entre 10 (= 37.5) y se lo resta a 100 para dar 62.5%

diferencia_con_max = 100 - alan_curso * 1000 // otros_cursos_promedio / 10

# Calculamos qué porcentaje es 1.5 respecto a 4 y se lo restamos a 100:

diferencia_con_promedio = 100 - alan_curso / otros_cursos_promedio * 100


# --- 3. MOSTRAR RESULTADOS EN PANTALLA ---
# Usamos f-strings (f'...') para insertar las variables calculadas directamente dentro del texto.
print(f'El curso de Alan dura un {diferencia_con_min_}% menos que el más rapido')
print (f'El curso de Alan dura un {diferencia_con_max}% menos que el más lento')
print (f'El curso de Alan dura un {diferencia_con_promedio}% menos que el promedio')




