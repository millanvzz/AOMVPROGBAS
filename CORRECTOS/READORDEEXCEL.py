import csv
import re
import numpy as np
import statistics as stats
import pandas as pd  # Para exportar a Excel
import os





# Lectura y validación de datos del archivo CSV
def leer_y_validar_csv(nombre_archivo):
    """
    Lee un archivo CSV de países, valida los campos y devuelve los datos listos para graficar.
    Cada país será representado como un diccionario con datos limpios y tipos adecuados.
    """
    datos_procesados = []
    errores = 0

    # Expresiones regulares
    regex_texto = r"^[\wÁÉÍÓÚÑáéíóúñ\s\(\)\-\,\.'’]+$"
    regex_divisa = r"^[\wÁÉÍÓÚÑáéíóúñ\s\(\)\-\,\.\$€¥£’ʻöđ]*$"
    regex_poblacion = r'^\d{1,3}(\.\d{3})*$'

    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            encabezados_esperados = {"nombre", "capital", "poblacion", "idioma", "divisa", "continente"}

            if set(lector.fieldnames) != encabezados_esperados:
                crear_csv_corregido(nombre_archivo)
                return []

            for i, fila in enumerate(lector, 1):
                nombre = fila['nombre'].strip()
                capital = fila['capital'].strip()
                poblacion_str = fila['poblacion'].strip()
                idioma = fila['idioma'].strip()
                divisa = fila['divisa'].strip()
                continente = fila['continente'].strip()
               

                # Validaciones
                if not re.match(regex_texto, nombre):
                    print(f"Fila {i}: nombre inválido → '{nombre}'")
                    errores += 1
                if not re.match(regex_texto, capital):
                    print(f"Fila {i}: capital inválida → '{capital}'")
                    errores += 1
                if not re.match(regex_poblacion, poblacion_str):
                    print(f"Fila {i}: población inválida → '{poblacion_str}'")
                    errores += 1
                if not re.match(regex_texto, idioma):
                    print(f"Fila {i}: idioma inválido → '{idioma}'")
                    errores += 1
                if not re.match(regex_divisa, divisa):
                    print(f"Fila {i}: divisa inválida → '{divisa}'")
                    errores += 1
                if not re.match(regex_texto, continente):
                    print(f"Fila {i}: continente inválido → '{continente}'")
                    errores += 1

                if errores == 0:
                    poblacion_num = int(poblacion_str.replace('.', ''))
                    datos_procesados.append({
                        "nombre": nombre,
                        "capital": capital,
                        "poblacion": poblacion_num,
                        "idioma": idioma,
                        "divisa": divisa,
                        "continente": continente
                    })

        if errores > 0:
            print(f"\nSe encontraron {errores} errores. Corrige el archivo antes de continuar.")
            return []
        else:
            return datos_procesados

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return []
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return []

# Análisis estadístico de población
def analizar_datos_poblacion(datos):
    poblaciones = [pais["poblacion"] for pais in datos]
    array = np.array(poblaciones)

    print("\nAnálisis Estadístico de la Población:\n")
    print(f"Cantidad de países: {len(poblaciones)}")
    print(f"Media: {np.mean(array):,.0f}")
    print(f"Mediana: {np.median(array):,.0f}")

    try:
        moda = stats.mode(poblaciones)
        print(f"Moda: {moda:,}")
    except:
        print("Moda: No se pudo calcular (posiblemente no hay valores repetidos)")

    print(f"Desviación estándar: {np.std(array):,.2f}")
    print(f"Varianza: {np.var(array):,.2f}")
    print(f"Valor mínimo: {np.min(array):,}")
    print(f"Valor máximo: {np.max(array):,}")
    print(f"Rango: {np.max(array) - np.min(array):,}")
    print(f"Percentil 25: {np.percentile(array, 25):,.0f}")
    print(f"Percentil 75: {np.percentile(array, 75):,.0f}")

    Q1 = np.percentile(array, 25)
    Q3 = np.percentile(array, 75)
    IQR = Q3 - Q1
    outliers = array[(array < Q1 - 1.5 * IQR) | (array > Q3 + 1.5 * IQR)]

    print(f"Outliers detectados (poblaciones extremas): {outliers if len(outliers) > 0 else 'Ninguno'}")

# Exportación a Excel por continente
def exportar_a_excel_por_continente(datos, continente_deseado):
    """
    Filtra los datos por continente y los exporta a un archivo Excel.
    """
    datos_filtrados = [pais for pais in datos if pais["continente"].lower() == continente_deseado.lower()]
    
    if not datos_filtrados:
        print(f"No se encontraron datos para el continente '{continente_deseado}'.")
        return

    df = pd.DataFrame(datos_filtrados)
    nombre_archivo = f"{continente_deseado.lower()}_paises.xlsx"
    df.to_excel(nombre_archivo, index=False)
    print(f"\n✅ Archivo Excel generado: '{nombre_archivo}'")

# Ejecución principal
if __name__ == "__main__":
    archivo = input("Ingresa el nombre del archivo CSV a procesar (ej. paises.csv): ").strip()
    datos = leer_y_validar_csv(archivo)

    if datos:
        print("\nDatos preparados correctamente.")
        print("Ejemplo de los primeros 3 países:\n")
        for pais in datos[:3]:
            print(pais)

        analizar_datos_poblacion(datos)

        continente = input("\nIngresa el nombre del continente para exportar (ej. Europa): ").strip()
        exportar_a_excel_por_continente(datos, continente)
        os.startfile(f"{continente}_paises.xlsx")


    else:
        print("\nNo se pudieron procesar los datos.")

def crear_csv_corregido(nombre_original):
    nuevo_nombre = "corregido_" + nombre_original
    encabezados = ['nombre', 'continente', 'capital', 'divisa', 'idioma', 'poblacion']

    with open(nuevo_nombre, mode='w', encoding='utf-8', newline='') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=encabezados)
        writer.writeheader()
    
    print(f"\n Encabezados incorrectos. Se creó un nuevo archivo vacío con encabezados correctos: '{nuevo_nombre}'")
    print("📝 Ábrelo y rellénalo con los datos correctos.")


