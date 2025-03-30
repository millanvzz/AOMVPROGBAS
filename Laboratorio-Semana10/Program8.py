def mergesort(lista):
    """
    Implementación del algoritmo Mergesort
    Recibe una lista de números y devuelve una nueva lista ordenada
    """
    # Caso base: lista vacía o con un solo elemento
    if len(lista) <= 1:
        return lista
    
    # Dividir la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    # Ordenar recursivamente cada mitad
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    
    # Combinar las mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    """
    Función auxiliar para combinar dos listas ordenadas
    """
    resultado = []
    i = j = 0
    
    # Comparar elementos y agregar el menor
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

def obtener_lista_numeros():
    """
    Solicita al usuario ingresar una lista de números separados por espacios
    """
    while True:
        entrada = input("Ingrese números separados por espacios: ").strip()
        if entrada:
            try:
                return [float(num) for num in entrada.split()]
            except ValueError:
                print("Error: Solo ingrese números separados por espacios")
        else:
            print("Error: No ingresó ningún número")

def main():
    print("=== ORDENAMIENTO CON MERGESORT ===")
    
    # Obtener lista del usuario
    lista = obtener_lista_numeros()
    print("\nLista original:")
    print(lista)
    
    # Ordenar la lista
    lista_ordenada = mergesort(lista)
    print("\nLista ordenada:")
    print(lista_ordenada)

if __name__ == "__main__":
    main()