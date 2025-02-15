number1 = int(input("Ingresa un número: ")) #variables a tomar en cuenta
number2 = int(input("Ingresar otro número: "))

elección = 0 #opcion para tomar valor despues

while elección != 6: #eleccion de operacion en ciclo
    print("""
    Indique la operación a realizar:

    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Cambio de valores
    6) Salir
    """)

    elección = int(input()) #eleccion tomando valor 

    if elección == 1: #procedimientos
        print(" ")
        print("Resultado: ", number1, "+", number2, "=", number1 + number2)

    if elección == 2:
        print(" ")
        print("Resultado: ", number1, "-", number2, "=", number1 - number2)

    if elección == 3:
        print(" ")
        print("Resultado: ", number1, "*", number2, "=", number1 * number2)

    if elección == 4:
        print(" ")
        print("Resultado: ", number1, "/", number2, "=", number1 / number2)

    if elección == 5:
        number1 = int(input("Ingresa un número: "))
        number2 = int(input("Ingresar otro número: "))

    if elección == 6:
        print("Gracias")
