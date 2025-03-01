#Calcular la suma de una serie numerica

print("Ingresa los números uno por uno. Escribe 'fin' para terminar.")
suma = 0
while True:
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
    if entrada.lower() == "fin":
       break
    try:
        numero = float(entrada)
        suma += numero
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número válido.")
print("La suma de los números ingresados es:", suma)