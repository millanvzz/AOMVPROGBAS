#Numeros al azar
import random

def imprimir_numeros_azar(n, a, b):
    for _ in range(n):
        print(random.randint(a, b))

#Entrada de datos
n = int(input("Ingrese la cantidad de números a generar: "))
a = int(input("Ingrese el valor mínimo: "))
b = int(input("Ingrese el valor máximo: "))

print("Números al azar:")
imprimir_numeros_azar(n, a, b)