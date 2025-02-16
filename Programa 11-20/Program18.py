#Suma de serie de numeros
# ingresar numeros
numeros = input("Ingrese una serie de números separados por espacios: ")

# Convertir la entrada en una lista de números
numeros_lista = list(map(float, numeros.split()))

# Calcular la suma de la serie
suma_total = sum(numeros_lista)

#Salida
print("La suma de la serie es:", suma_total)