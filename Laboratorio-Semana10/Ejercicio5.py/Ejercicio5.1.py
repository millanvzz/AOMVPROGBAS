import conversor

def mostrar_menu():
    print("\n" + "="*30)
    print("   CONVERSOR DE UNIDADES")
    print("="*30)
    print("1. Kilómetros a Millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a Galones")
    print("4. Salir")
    print("="*30)

def obtener_numero(mensaje: str) -> float:
    """Obtiene un número válido del usuario"""
    while True:
        try:
            valor = input(mensaje).strip()
            if valor.replace('.', '', 1).isdigit():  # Permite decimales
                return float(valor)
            raise ValueError
        except ValueError:
            print("ERROR: Debe ingresar un número válido)")

def main():
    print("\nConversor de unidades")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            km = obtener_numero("Ingrese kilómetros: ")
            print(f"\n{km} km = {conversor.km_a_millas(km):.4f} millas")
        
        elif opcion == "2":
            c = obtener_numero("Ingrese grados Celsius: ")
            print(f"\n{c}°C = {conversor.celsius_a_fahrenheit(c):.4f}°F")
        
        elif opcion == "3":
            l = obtener_numero("Ingrese litros: ")
            print(f"\n{l} litros = {conversor.litros_a_galones(l):.4f} galones")
        
        elif opcion == "4":
            print("\nGracias por usar el conversor")
            break
        
        else:
            print("\nERROR: Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()