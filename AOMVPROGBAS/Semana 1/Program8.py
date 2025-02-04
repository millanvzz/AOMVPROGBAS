import math

def calcirculo(radio):
    area = math.pi * radio ** 2
    circunferencia = 2 * math.pi * radio
    return area, circunferencia

radio = float(input("Ingrese el radio del círculo: "))
area, circunferencia = calcirculo(radio)

print(f"Área: {area:2f}")
print(f"Circunferencia: {circunferencia:2f}")
