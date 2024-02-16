import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def calcular_distancia():
    cp_salida = entrada_salida.get()
    cp_llegada = entrada_llegada.get()
    
    geolocalizador = Nominatim(user_agent="calculo-distancia")
    
    # Obtener las coordenadas (latitud, longitud) de los códigos postales
    location_salida = geolocalizador.geocode(cp_salida)
    location_llegada = geolocalizador.geocode(cp_llegada)
    
    if location_salida is None or location_llegada is None:
        messagebox.showerror("Error", "No se pudo encontrar la ubicación para uno o ambos códigos postales.")
        return
    
    # Crear tuplas de coordenadas (latitud, longitud)
    coords_salida = (location_salida.latitude, location_salida.longitude)
    coords_llegada = (location_llegada.latitude, location_llegada.longitude)
    
    # Calcular la distancia entre las coordenadas
    distancia = geodesic(coords_salida, coords_llegada).kilometers
    
    messagebox.showinfo("Distancia", f"La distancia entre los códigos postales {cp_salida} y {cp_llegada} es de {distancia:.2f} kilómetros.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Distancia entre Códigos Postales")

# Crear etiquetas y cuadros de texto para los códigos postales
etiqueta_salida = tk.Label(ventana, text="Código Postal de Salida:")
etiqueta_salida.grid(row=0, column=0, padx=5, pady=5)

entrada_salida = tk.Entry(ventana)
entrada_salida.grid(row=0, column=1, padx=5, pady=5)

etiqueta_llegada = tk.Label(ventana, text="Código Postal de Llegada:")
etiqueta_llegada.grid(row=1, column=0, padx=5, pady=5)

entrada_llegada = tk.Entry(ventana)
entrada_llegada.grid(row=1, column=1, padx=5, pady=5)

# Botón para calcular la distancia
boton_calcular = tk.Button(ventana, text="Calcular Distancia", command=calcular_distancia)
boton_calcular.grid(row=2, columnspan=2, padx=5, pady=5)

# Ejecutar el bucle de eventos
ventana.mainloop()
