# Grafica_Medidas_unidad_academica.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np
import os

carpeta_destino = 'Graficas_Datos_Generales'
# Crear carpeta si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)


df = pd.read_csv('Medidas_unidad_academica.csv') # Cargar datos de medidas
# Convertimos a diccionario para fácil acceso
medidas = dict(zip(df['Medidas'], df['Metros'])) # Llave: Nombre de la medida, Valor: Metros

# Se definen coordenadas basadas en las medidas
enfrente = medidas['Enfrente'] # Medida frontal
atras = medidas['Atras'] # Medida trasera
lat_der = medidas['Lateral derecho'] # Medida lateral derecha
lat_izq = medidas['Lateral izquierda'] # Medida lateral izquierda

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
fig, ax = plt.subplots(figsize=(8, 10)) # Tamaño de la figura
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
plt.grid(True, linestyle=':', alpha=0.6) # Cuadrícula
plt.xlabel('Metros (X)') # Etiqueta eje X
plt.ylabel('Metros (Y)') # Etiqueta eje Y

plt.tight_layout() # Ajustar el diseño para evitar recortes
# Guardar la gráfica
nombre_img = "Grafica_Perimetro_area.png" # Nombre del archivo de la imagen
plt.savefig(os.path.join(carpeta_destino, nombre_img), dpi=400, bbox_inches='tight') # Guardar la imagen
plt.show() # Mostrar la gráfica

# Por ultimo guardar los resultados en un archivo de texto
with open('Reporte_Medidas.txt', 'w') as f: # Abrir archivo para escribir
    f.write(f"Proyecto: Cada Gota Cuenta Cada Residuo Transforma\n") # Título del proyecto
    f.write(f"Resultados de investigación:\n") # Encabezado
    f.write(f"Área Total: {area:.2f} m2\n") # Escribir resultado área
    f.write(f"Perímetro: {perimetro:.2f} m\n") # Escribir resultado perímetro

print("\nGráfica generada y reporte guardado exitosamente.") # Confirmación de éxito