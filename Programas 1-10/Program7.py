def vernum(numero, multde): #operacion a retornar
    if numero == 0:
        print("0 es neutro")
    elif numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")
    
    if numero % multde == 0:
        print(f"{numero} es múltiplo de {multde}.")
    else:
        print(f"{numero} no es múltiplo de {multde}.")

num = int(input("Ingresa un número: "))
multiplo = int(input("Ingresa el número para verificar si es múltiplo: "))
vernum(num, multiplo)
