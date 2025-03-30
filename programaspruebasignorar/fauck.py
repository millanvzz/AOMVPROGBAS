def esfuck(n):
    if n < 0:
        return "no se puede sacar el factorial de un negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1): #secuencia de numeros
            resultado *= i
        return resultado
num = int(input("Ingresa un número: "))
print(f"El factorial de {num} es {esfuck(num)}") #salida