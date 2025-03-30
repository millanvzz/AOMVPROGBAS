import random

# Genera una lista de números aleatorios
def generar_lista_aleatoria(longitud, rango_min, rango_max):
    return [random.randint(rango_min, rango_max) for _ in range(longitud)]

# Implementación del algoritmo Quicksort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + medio + quicksort(derecha)

# Implementación de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Función principal del programa
def main():
    print("=== PROGRAMA DE ORDENAMIENTO Y BÚSQUEDA ===")
    
    # Generar lista aleatoria
    lista = generar_lista_aleatoria(20, 1, 100)
    print("\nLista original:")
    print(lista)
    
    # Ordenar la lista
    lista_ordenada = quicksort(lista)
    print("\nLista ordenada con Quicksort:")
    print(lista_ordenada)
    
    # Búsqueda binaria
    try:
        objetivo = int(input("\nIngrese un número para buscar: "))
        resultado = busqueda_binaria(lista_ordenada, objetivo)
        
        if resultado != -1:
            print(f"\nEl número {objetivo} se encuentra en la posición {resultado}")
        else:
            print(f"\nEl número {objetivo} no se encuentra en la lista")
    except ValueError:
        print("Error: Debe ingresar un número entero válido")

if __name__ == "__main__":
    main()