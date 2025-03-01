# calcular inversa de matriz
import numpy as np

# Definir la matriz
A = np.array([[2, 3], 
              [1, 4]])

# Calcular la inversa
try:
    A_inv = np.linalg.inv(A)
    print("Matriz inversa:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("La matriz no es invertible.")