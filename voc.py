import requests
import re
from typing import Optional, Dict, List

class RestCountriesAPI:
    BASE_URL = "https://restcountries.com/v3.1"
    
    def __init__(self):
        self.session = requests.Session()
    
    def _make_request(self, endpoint: str) -> Optional[Dict]:
        """Realiza una petición a la API y maneja errores"""
        try:
            response = self.session.get(f"{self.BASE_URL}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            return None
    
    def validar_codigo_pais(self, codigo: str) -> bool:
        """Valida un código de país (alpha-2 o alpha-3) usando regex"""
        return bool(re.match(r'^[A-Za-z]{2,3}$', codigo))
    
    def obtener_info_pais(self, codigo_pais: str) -> Optional[Dict]:
        """Obtiene información de un país por su código"""
        if not self.validar_codigo_pais(codigo_pais):
            print("Código de país no válido. Debe ser de 2 o 3 letras.")
            return None
        
        return self._make_request(f"alpha/{codigo_pais.lower()}")
    
    def obtener_paises_por_moneda(self, moneda: str) -> Optional[List[Dict]]:
        """Obtiene países que usan una moneda específica"""
        if not re.match(r'^[A-Za-z]{3}$', moneda):
            print("Código de moneda no válido. Debe ser de 3 letras.")
            return None
        
        return self._make_request(f"currency/{moneda.lower()}")
    
    def contar_total_paises(self) -> int:
        """Cuenta el total de países disponibles en la API"""
        paises = self._make_request("all")
        return len(paises) if paises else 0
    
    def buscar_paises_por_nombre(self, nombre: str) -> Optional[List[Dict]]:
        """Busca países por nombre"""
        if not re.match(r'^[A-Za-z\s]{2,}$', nombre):
            print("Nombre no válido. Solo letras y espacios, mínimo 2 caracteres.")
            return None
        
        return self._make_request(f"name/{nombre}")


# Ejemplo de uso
if __name__ == "__main__":
    api = RestCountriesAPI()
    
    # Consulta básica: ¿Cuántos países hay en total?
    total_paises = api.contar_total_paises()
    print(f"\nHay {total_paises} países en la base de datos.\n")
    
    # Obtener información de un país específico (ej: México)
    codigo = input("Ingresa un código de país (ej. MX, USA, BRA): ").strip()
    info_pais = api.obtener_info_pais(codigo)
    
    if info_pais:
        pais = info_pais[0]  # La API devuelve una lista incluso para un solo país
        print(f"\nInformación de {pais['name']['common']}:")
        print(f"Capital: {', '.join(pais.get('capital', ['No disponible']))}")
        print(f"Población: {pais.get('population', 'No disponible'):,}")
        print(f"Moneda: {', '.join(pais.get('currencies', {}).keys())}")
        print(f"Región: {pais.get('region', 'No disponible')}")
    
    # Buscar países por moneda (ej: USD)
    moneda = input("\nIngresa un código de moneda para buscar (ej. USD, EUR, MXN): ").strip()
    paises_moneda = api.obtener_paises_por_moneda(moneda)
    
    if paises_moneda:
        print(f"\nPaíses que usan {moneda.upper()}:")
        for pais in paises_moneda:
            print(f"- {pais['name']['common']}")