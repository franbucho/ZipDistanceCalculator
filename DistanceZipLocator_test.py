from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def calcular_distancia(cp1, cp2):
    geolocalizador = Nominatim(user_agent="calculo-distancia")
    
    # Obtener las coordenadas (latitud, longitud) de los códigos postales
    location1 = geolocalizador.geocode(cp1)
    location2 = geolocalizador.geocode(cp2)
    
    if location1 is None or location2 is None:
        return "No se pudo encontrar la ubicación para uno o ambos códigos postales."
    
    # Crear tuplas de coordenadas (latitud, longitud)
    coords1 = (location1.latitude, location1.longitude)
    coords2 = (location2.latitude, location2.longitude)
    
    # Calcular la distancia entre las coordenadas
    distancia = geodesic(coords1, coords2).kilometers
    return distancia

# Ejemplo de uso
codigo_postal1 = "10001"  # Código postal de Nueva York
codigo_postal2 = "90210"  # Código postal de Beverly Hills

distancia = calcular_distancia(codigo_postal1, codigo_postal2)
print(f"La distancia entre los códigos postales {codigo_postal1} y {codigo_postal2} es de {distancia:.2f} kilómetros.")
