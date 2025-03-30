def ubicadorDeVocales(cadena):
    conteo = {v: [] for v in "aeiou"}  # Inicializar diccionario con listas vacías para cada vocal
    
    for i, letra in enumerate(cadena):
        letra_min = letra.lower()
        if letra_min in conteo:
            conteo[letra_min].append(i)
    
    return conteo

# Pruebas
print(ubicadorDeVocales("murcielago"))
print(ubicadorDeVocales("eucalipto"))
print(ubicadorDeVocales("Albericoque"))
