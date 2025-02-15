def convertir_temperatura(valor, escala_origen, escala_destino):
    if escala_origen == "C":
        if escala_destino == "F":
            return (valor * 9/5) + 32
        elif escala_destino == "K":
            return valor + 273.15
    elif escala_origen == "F":
        if escala_destino == "C":
            return (valor - 32) * 5/9
        elif escala_destino == "K":
            return (valor - 32) * 5/9 + 273.15
    elif escala_origen == "K":
        if escala_destino == "C":
            return valor - 273.15
        elif escala_destino == "F":
            return (valor - 273.15) * 9/5 + 32
    return None

valor = float(input("Ingresa el valor de la temperatura: "))
escala_origen = input("Ingresa la escala de origen (C, F, K): ").upper()
escala_destino = input("Ingresa la escala de destino (C, F, K): ").upper()

resultado = convertir_temperatura(valor, escala_origen, escala_destino)
if resultado is not None:
    print(f"{valor}°{escala_origen} equivale a {resultado:.2f}°{escala_destino}")
else:
    print("Escalas no válidas. Usa C, F o K.")