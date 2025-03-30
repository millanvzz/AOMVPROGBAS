def suma_digitos(n):
    if n < 0:
        print("El número no debe ser negativo")
        return None
    return sum(int(d) for d in str(n))


numero = int(input("Ingresa un número: "))
resultado = suma_digitos(numero)
if resultado is not None:
    print("Suma de los dígitos:", resultado)