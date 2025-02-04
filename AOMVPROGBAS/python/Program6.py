def interes_compuesto(capital, tasa, tiempo): #operacion a retornar
    monto_final = capital * (1 + tasa) ** tiempo
    return monto_final

capital_inicial = float(input("Ingrese el capital inicial: ")) #operaciones
tasa_interes = float(input("Ingrese la tasa de interés anual en porcentaje: ")) / 100
tiempo_anios = int(input("Ingrese el tiempo en años: "))

monto = interes_compuesto(capital_inicial, tasa_interes, tiempo_anios)
print(f"El monto final después de {tiempo_anios} años será: {monto:.2f}") #salida
