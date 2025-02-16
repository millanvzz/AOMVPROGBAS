#Conversor de unidades
def convertir_longitud(valor, unidad_origen, unidad_destino): #funcion
    factores = {
        "m": 1, "km": 0.001, "mi": 0.000621371, "ft": 3.28084
    }
    if unidad_origen in factores and unidad_destino in factores:
        return valor * (factores[unidad_destino] / factores[unidad_origen])
    return None

def convertir_masa(valor, unidad_origen, unidad_destino): #funcion
    factores = {
        "g": 1, "kg": 0.001, "lb": 0.00220462, "oz": 0.035274
    }
    if unidad_origen in factores and unidad_destino in factores:
        return valor * (factores[unidad_destino] / factores[unidad_origen])
    return None

def convertir_temperatura(valor, unidad_origen, unidad_destino): #funcion
    if unidad_origen == "C" and unidad_destino == "F":
        return (valor * 9/5) + 32
    elif unidad_origen == "C" and unidad_destino == "K":
        return valor + 273.15
    elif unidad_origen == "F" and unidad_destino == "C":
        return (valor - 32) * 5/9
    elif unidad_origen == "F" and unidad_destino == "K":
        return (valor - 32) * 5/9 + 273.15
    elif unidad_origen == "K" and unidad_destino == "C":
        return valor - 273.15
    elif unidad_origen == "K" and unidad_destino == "F":
        return (valor - 273.15) * 9/5 + 32
    return None

# Menú principal
print("\n--- Conversor de Unidades ---")
print("1. Longitud (m, km, mi, ft)")
print("2. Masa (g, kg, lb, oz)")
print("3. Temperatura (C, F, K)")

opcion = input("Seleccione una categoría (1-3): ") #eleccion de categoria

valor = float(input("\nIngrese el valor a convertir: "))
unidad_origen = input("Ingrese la unidad de origen: ").strip()
unidad_destino = input("Ingrese la unidad de destino: ").strip()

if opcion == "1":
    resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
elif opcion == "2":
    resultado = convertir_masa(valor, unidad_origen, unidad_destino)
elif opcion == "3":
    resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
else:
    resultado = None

if resultado is not None:
    print(f"\n{valor} {unidad_origen} equivale a {resultado:.4f} {unidad_destino}")
else:
    print("\nConversión no válida. Revise las unidades ingresadas.")
