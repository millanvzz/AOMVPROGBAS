#Codigo para contar vocales y consonantes en una cadena
def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    num_vocales = sum(1 for c in cadena if c in vocales)
    num_consonantes = sum(1 for c in cadena if c in consonantes)

    return num_vocales, num_consonantes

# Entrada del usuario
cadena = input("Ingrese una cadena de texto: ")

# Obtener los conteos
total_vocales, total_consonantes = contar_vocales_consonantes(cadena)

# Mostrar resultados
print(f"\nNúmero de vocales: {total_vocales}")
print(f"Número de consonantes: {total_consonantes}")