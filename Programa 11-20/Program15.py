#Codigo para resolver ecuaciones cuadraticas
import cmath

def solve_quadratic(a, b, c): #Funcion principal
    if a == 0:
        return "No es una ecuación cuadrática (a no puede ser 0)"
    
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)
    
    return x1, x2

# Entrada de datos
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

soluciones = solve_quadratic(a, b, c)
print("Las soluciones son:", soluciones)#salida
