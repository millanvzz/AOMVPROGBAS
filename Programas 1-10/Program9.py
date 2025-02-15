def numeros_anteriores(n): #operacion a retornar
    for i in range(n - 1, 0, -1): 
        clasif = "par" if i % 2 == 0 else "impar"
        print(f"{i} es {clasif}")

numero = int(input("Introduce un número: "))
numeros_anteriores(numero) #salida
