#Implementar funciones recursivas

# Función recursiva para calcular el factorial de un número
def factorial(n):
    if n == 0:                              #Caso base: factorial de 0 es 1
        return 1
    else:                                   #Caso recursivo: factorial de n es n * factorial de (n-1)
        return n * factorial(n - 1)

numero = int(input("Ingresa un número para calcular su factorial: "))
resultado = factorial(numero)
print("El factorial de:",numero, "es:", resultado)