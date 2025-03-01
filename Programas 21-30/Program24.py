#Generar y analizar un histogramas de datos
"""
pip install --upgrade mathplot numpy
pip install mathplot numpy
"""

import matplotlib.pyplot as plt
import numpy as np

def generar_histograma():
    datos = list(map(int, input("Ingrese los datos separados por espacios: ").split()))
    bins = int(input("Ingrese el número de bins: "))
    
    plt.hist(datos, bins=bins, edgecolor='black')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Datos')
    plt.show()
    
    print(f"Media: {np.mean(datos)}")
    print(f"Mediana: {np.median(datos)}")
    print(f"Desviación estándar: {np.std(datos)}")

generar_histograma()