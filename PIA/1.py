
import requests #importar la libreria para hacer las peticiones

def comprobar_internet(): # Esta función revisa si hay conexión a internet
    try:
        requests.get("https://www.google.com", timeout=3)
        return True # Si se puede conectar, regresa True
    except requests.ConnectionError:
        return False # Si no hay conexión, regresa False

def obtener_paises(): # Esta función consulta la API de países y por lo pronto muestra nada mas sus nombres y sus capitales
    url = "https://restcountries.com/v3.1/all" # URL de la API
    response = requests.get(url)

    if response.status_code == 200: #Codigo para la correcta ejecucion del API
        countries = response.json()
        for country in countries:
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0]
            print(f"{name} - Capital: {capital}") #Impresion
    else:
        print(f"Error al consultar la API. Código de estado: {response.status_code}") #Mensaje de error

if comprobar_internet():
    print("Conexión a internet detectada. Consultando API...") #Impresion de exito al agarrar la conexion
    obtener_paises()
else:
    print("No hay conexión a internet. Verifica tu red.") #Impresion de error al agarrar la conexion
print("Fin del programa") #Salida del programa 