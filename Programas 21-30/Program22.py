#Implementar y operar matrices

def crear_matriz(filas, columnas):
    return [[int(input(f"Elemento [{i}][{j}]: ")) for j in range(columnas)] for i in range(filas)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))
matriz = crear_matriz(filas, columnas)
    
print("Matriz generada:")
imprimir_matriz(matriz)