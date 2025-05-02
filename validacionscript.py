#INICIO DEL SCRIPT DE LA SEMANA 3

import csv  # Librería para trabajar con archivos CSV
import re

def leer_datos_csv(nombre_archivo):
    """Lee el archivo CSV y muestra los datos de cada país"""
    try:   # Abrimos el archivo en modo lectura

        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # DictReader lee los datos como diccionarios

            print("\n--- Datos del archivo ---\n")

            for i, fila in enumerate(lector, 1): # Recorrer cada fila del archivo y mostrar los datos
                print(f"{i}. {fila['nombre']}")
                print(f"   Capital   : {fila['capital']}")
                print(f"   Población : {fila['poblacion']}")
                print(f"   Idioma    : {fila['idioma']}")
                print(f"   Divisa    : {fila['divisa']}\n")

    except FileNotFoundError:  # Si el archivo no existe = error

        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:

        print(f"Ocurrió un error al leer el archivo: {e}")


def validar_formato(nombre_archivo):
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
       lector = csv.DictReader(archivo)
       regex_linea = r'^[A-ZÁÉÍÓÚÑa-záéíóúñ\s\(\)]+$'
       regex_poblacion = r'^\d{1,3}(\.\d{3})*$'
       for i, fila in enumerate(lector, 1):
           if not re.match(regex_linea, fila['nombre'].strip()):
              print(f"Fila {i}: nombre inválido → '{fila['nombre']}'")
              return False
           if not re.match(regex_linea, fila['capital'].strip()):
              print(f"Fila {i}: capital inválida → '{fila['capital']}'")
              return False
           if not re.match(regex_poblacion, fila['poblacion'].strip()):
              print(f"Fila {i}: población inválida → '{fila['poblacion']}'")
              return False
           if not re.match(regex_linea, fila['idioma'].strip()):
              print(f"Fila {i}: idioma inválido → '{fila['idioma']}'")
              return False
           if not re.match(regex_linea, fila['divisa'].strip()):
              print(f"Fila {i}: divisa inválida → '{fila['divisa']}'")
              return False


if __name__ == "_main_":
    # Pedir el nombre del archivo a leer
    archivo = input("Ingresa el nombre del archivo CSV a leer (ej. africa_paises.csv): ").strip()
    leer_datos_csv(archivo)  # Llamamos a la función y mostrar los datos