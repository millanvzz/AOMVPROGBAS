def ubicadorDeVocales(cadena):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    ubicaciones_vocales = {}
    
    for indice, caracter in enumerate(cadena):
        if caracter in vocales:
            if caracter not in ubicaciones_vocales:
                ubicaciones_vocales[caracter] = []
            ubicaciones_vocales[caracter].append(indice)
    
    return ubicaciones_vocales

# Pruebas
print(ubicadorDeVocales("murcielago"))
print(ubicadorDeVocales("eucalipto"))
print(ubicadorDeVocales("Albericoque"))

