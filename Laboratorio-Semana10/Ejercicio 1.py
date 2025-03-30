def analizar_texto(texto):
    palabras = texto.lower().split()
    total_palabras = len(palabras)
    palabras_unicas = set(palabras)
    frecuencia_palabras = {}
    
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    
    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    frecuencia_max = frecuencia_palabras[palabra_mas_frecuente]
    
    print("\nResumen del análisis del texto:")
    print(f"- Número total de palabras: {total_palabras}")
    print(f"- Cantidad de palabras únicas: {len(palabras_unicas)}")
    print("- Frecuencia de cada palabra:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"  {palabra}: {frecuencia}")
    print(f"- La palabra más frecuente es '{palabra_mas_frecuente}' con {frecuencia_max} apariciones.")

# Solicitar texto al usuario
txt = input("Ingresa un texto: ")
analizar_texto(txt)
