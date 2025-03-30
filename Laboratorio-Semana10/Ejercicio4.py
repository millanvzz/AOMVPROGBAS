def calcular_estadisticas(*args):
    
    if not args:
        return None, None, None
    
    datos = list(args)
    n = len(datos)
    
    #  Cálculo del promedio
    promedio = (lambda x: sum(x)/len(x))(datos)
    
    #  Cálculo de la mediana
    datos_ordenados = sorted(datos)
    mitad = n // 2
    
    if n % 2 == 1:
        mediana = datos_ordenados[mitad]
    else:
        mediana = (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
    
    #  Cálculo de la desviación estándar 
    suma_cuadrados = sum((x - promedio)**2 for x in datos)
    varianza = suma_cuadrados / n
    
    # Aproximación de raíz cuadrada 
    if varianza == 0:
        desviacion = 0.0
    else:
        
        raiz = varianza / 2
        for _ in range(20):  
            raiz = (raiz + varianza/raiz) / 2
        desviacion = raiz
    
    return promedio, mediana, desviacion

def main():
    print("'Calculadora'")
    print("Ingrese números separados por espacios (ej: 1 2 3 4 5):")
    
    try:
        entrada = input("> ")
        numeros = [float(x) for x in entrada.split()]
        
        if not numeros:
            print("Error: No se ingresaron números")
            return
        
        prom, med, desv = calcular_estadisticas(*numeros)
        
        print("\nResultados:")
        print(f"• Promedio: {prom:.4f}")
        print(f"• Mediana: {med:.4f}")
        print(f"• Desviación estándar: {desv:.4f}")
    
    except ValueError:
        print("Error: Solo ingrese números separados por espacios")

if __name__ == "__main__":
    main()