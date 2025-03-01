#Generar y analizar datos estadisticos

import statistics
import random

Tot_Datos= int(input("Introduzca la cantidad de datos que desea generar: "))
datos = [random.randint(1, Tot_Datos) for _ in range(Tot_Datos)]

# Calcular estadísticas
promedio = statistics.mean(datos)
mediana = statistics.median(datos)
des_est = statistics.stdev(datos)

print("Datos:",datos)
print("Promedio:", promedio)
print("Mediana:", mediana)
print("Desviación Estándar:", des_est)