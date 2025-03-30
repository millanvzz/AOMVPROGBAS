
from modulo_operaciones import suma, resta, es_par
from clases import Rectangulo

# Paradigma Estructurado
def mostrar_menu():
    """Muestra el menú principal"""
    print("\n=== DEMOSTRACIÓN MULTI-PARADIGMA ===")
    print("1. Ejemplo Imperativo")
    print("2. Ejemplo Estructurado")
    print("3. Ejemplo Modular")
    print("4. Ejemplo OOP")
    print("5. Salir")

def ejemplo_estructurado():
    """Demuestra programación estructurada"""
    print("\n--- Paradigma Estructurado ---")
    a = float(input("Ingrese primer número: "))
    b = float(input("Ingrese segundo número: "))
    resultado = suma(a, b) * resta(a, b)
    print(f"({a} + {b}) * ({a} - {b}) = {resultado}")

# Paradigma Imperativo
def ejemplo_imperativo():
    """Demuestra programación imperativa"""
    print("\n--- Paradigma Imperativo ---")
    numero = int(input("Ingrese un número: "))
    
    # Condicionales
    if numero > 10:
        print(f"{numero} es mayor que 10")
    elif numero == 10:
        print("El número es 10")
    else:
        print(f"{numero} es menor que 10")
    
    # Bucles
    print("Números pares hasta 10:")
    contador = 0
    while contador <= 10:
        if contador % 2 == 0:
            print(contador, end=" ")
        contador += 1
    print()

# Función principal
def main():
    """Controlador principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            ejemplo_imperativo()
        elif opcion == "2":
            ejemplo_estructurado()
        elif opcion == "3":
            print("\n--- Paradigma Modular ---")
            num = int(input("Ingrese un número: "))
            print(f"¿{num} es par? {es_par(num)}")
        elif opcion == "4":
            print("\n--- Paradigma OOP ---")
            rect = Rectangulo(4, 5)
            print(f"Área del {rect.nombre}: {rect.area()}")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()