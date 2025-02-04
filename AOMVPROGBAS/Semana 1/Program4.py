def seriefib(n):
    fibonacci = [0, 1]
    while True:
        seguir = fibonacci[-1] + fibonacci[-2]
        if seguir > n:
            break
        fibonacci.append(seguir)
    return fibonacci

numero = int(input("Ingrese un número límite: "))
print(f"Secuencia de Fibonacci hasta {numero}: {seriefib(numero)}")
