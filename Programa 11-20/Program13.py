#Conversion de temperaturas
def convertir_temperatura(valor, escala_entrada, escala_salida): #Funcion principal
   #Todos los procsos de la funcion
    if escala_entrada == "C":
        if escala_salida == "F":
            return (valor * 9/5) + 32
        elif escala_salida == "K":
            return valor + 273.15
    elif escala_entrada == "F":
        if escala_salida == "C":
            return (valor - 32) * 5/9
        elif escala_salida == "K":
            return (valor - 32) * 5/9 + 273.15
    elif escala_entrada == "K":
        if escala_salida == "C":
            return valor - 273.15
        elif escala_salida == "F":
            return (valor - 273.15) * 9/5 + 32
    return None

valor = float(input("Ingresa el valor de la temperatura: ")) #Entrada de datos
escala_entrada = input("Ingresa la escala de origen (C, F, K): ").upper()
escala_salida= input("Ingresa la escala de destino (C, F, K): ").upper()

resultado = convertir_temperatura(valor, escala_entrada, escala_salida) #Salida
if resultado is not None:
    print(f"{valor}°{escala_entrada} equivale a {resultado:.2f}°{escala_salida}")
else:
    print("Escalas no válidas. Usa C, F o K.")