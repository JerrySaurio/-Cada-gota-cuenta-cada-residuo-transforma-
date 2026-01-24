# Grafica_Medidas_unidad_academica.py
from Config_rutas import CARPETA_DATOS, CARPETA_RESULTADOS, CARPETA_GRAFICAS
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np
import os
import sys

CONFIG_UI = {
    "nombre_proyecto": 'Captación de agua pluvial y gestión de residuos.\n"Cada gota cuenta cada residuo transforma"',
    "institucion": "Universidad Nacional Rosario Castellanos",
    "autor": 'Equipo 3',
}

# FUNCIÓN CARGA SEGURA CSV
def cargar_csv(nombre_archivo):
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)
    try:
        return pd.read_csv(ruta)
    except FileNotFoundError:
        print(f"\nERROR: No se encontró el archivo:\n{ruta}")
        print("Verifica que la carpeta 'Datos_recopilados' exista y contenga el CSV.")
        sys.exit()

def Grafica_Medidas():
    
    df = cargar_csv("Medidas_unidad_academica.csv") # Cargar archivo CSV de medidas
    # Convertimos a diccionario para fácil acceso
    medidas = dict(zip(df['Medidas'], df['Metros'])) # Llave: Nombre de la medida, Valor: Metros

    # Se definen coordenadas basadas en las medidas
    try:
        enfrente = medidas['Enfrente'] # Medida frontal
        atras = medidas['Atras'] # Medida trasera
        lat_der = medidas['Lateral derecho'] # Medida lateral derecha
        lat_izq = medidas['Lateral izquierda'] # Medida lateral izquierda
    except KeyError:
        print("\nERROR: Nombres de columnas incorrectos en Medidas_unidad_academica.csv")
        sys.exit()

    # Proyectamos los puntos (aproximación de trapezoide)
    vertices = [
        (0, 0),                          # A: Inicio Enfrente, P1 de origen
        (enfrente, 0),                   # B: Fin Enfrente, P2 esquina frontal derecha
        (atras, lat_der),                # C: Fin Atrás, P3 esquina trasera derecha
        (0, lat_izq)                     # D: Inicio Atrás, P4 esquina trasera izquierda
    ]

    # Cálculo de perímetro y área
    perimetro = enfrente + lat_der + atras + lat_izq # Cálculo del perímetro
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1))) # Fórmula del área del polígono

    # Configuración de la visualización
    fig, ax = plt.subplots(figsize=(8, 9), dpi= 100) # Tamaño de la figura
    terreno = patches.Polygon(vertices, closed=True, facecolor="#d1e7dd", edgecolor="#0f5132", lw=2) # Polígono del terreno
    ax.add_patch(terreno) # Añadir el polígono del terreno

    # Se anotan las medidas en el gráfico para veracidad
    ax.text(enfrente/2, -5, f"Enfrente: {enfrente}m", ha='center') # Medida enfrente
    ax.text(atras/2, max(lat_der, lat_izq) + 2, f"Atrás: {atras}m", ha='center') # Medida atrás
    ax.text(-10, lat_izq/2, f"Lateral Izq: {lat_izq}m", va='center', rotation=90) # Medida lateral izquierda
    ax.text(enfrente + 5, lat_der/2, f"Lateral Der: {lat_der}m", va='center', rotation=270) # Medida lateral derecha

    # Información de perímetro y área en el gráfico
    info_text = f"Perímetro: {perimetro:.2f}m   Área: {area:.2f}m²" # Texto informativo
    props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='#969696FF') # Estilo del recuadro
    ax.text(0.26, 0.95, info_text, transform=ax.transAxes, fontsize=11.2,
            verticalalignment='center', bbox=props, fontfamily='Arial') # Añadir texto al gráfico

    # Ajustes finales de la gráfica
    ax.set_xlim(-20, enfrente + 20) # Límites del eje X
    ax.set_ylim(-10, max(lat_der, lat_izq) + 15) # Límites del eje Y
    ax.set_aspect('equal') # Proporción igual
    plt.title(f"Dimensiones de la unidad académica", pad=20, fontsize=14, fontweight='bold') # Título
    plt.xlabel('Metros (X)') # Etiqueta eje X
    plt.ylabel('Metros (Y)') # Etiqueta eje Y
    plt.grid(True, linestyle=':', alpha=0.6) # Cuadrícula

    plt.tight_layout() # Ajustar el diseño para evitar recortes

    # Guardar la gráfica
    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_Perimetro_Area.png") # Nombre del archivo de la imagen
    plt.savefig(ruta_img, dpi=400, bbox_inches='tight') # Guardar la imagen

    # Por ultimo guardar los resultados en un archivo de texto
    ruta_reporte = os.path.join(CARPETA_RESULTADOS, "Reporte_Medidas.txt")

    with open(ruta_reporte, "w", encoding="utf-8") as f: # Abrir archivo para escribir
        f.write(CONFIG_UI["nombre_proyecto"] + "\n") # Título del proyecto
        f.write(CONFIG_UI["institucion"] + "\n") # Nombre de la Institución
        f.write("="*60 + "\n\n")
        f.write("Resultados de medición de la unidad académica\n\n") # Encabezado
        f.write(f"Área total: {area:.2f} m²\n") # Escribir resultado área
        f.write(f"Perímetro total: {perimetro:.2f} m\n") # Escribir resultado perímetro

if __name__ == "__main__":
    Grafica_Medidas()