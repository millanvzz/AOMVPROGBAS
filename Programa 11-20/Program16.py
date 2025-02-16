#Lanzamiento de dado y moneda
import random

def lanzar_dado():
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

#Ya se pone el lanzamiento de ambos
dado = lanzar_dado()
moneda = lanzar_moneda()

print("Resultado del dado:", dado)
print("Resultado de la moneda:", moneda)
