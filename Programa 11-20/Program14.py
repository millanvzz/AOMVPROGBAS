def es_bisiesto(a):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return True
    return False

a = int(input("Ingresa un año: "))

if es_bisiesto(a):
    print(f"El año {a} es bisiesto.")
else:
    print(f"El año {a} no es bisiesto.")