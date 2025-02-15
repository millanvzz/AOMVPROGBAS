def factorial(n):
    if n < 0: #no se puede sacar factorial de un negativo
        return "No se puede calcular el factorial de un número negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1): #secuencia de numeros
            resultado *= i
        return resultado
num = int(input("Ingresa un número: "))
print(f"El factorial de {num} es {factorial(num)}") #salida