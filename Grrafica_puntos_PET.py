import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import os

carpeta_destino = 'Graficas_Datos_Generales'
# Crear carpeta si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)
df = pd.read_csv('Medidas_unidad_academica.csv') # Cargar datos de medidas
medidas = dict(zip(df['Medidas'], df['Metros'])) # Convertimos a diccionario para fácil acceso. Llave: Nombre de la medida, Valor: Metros

# Se definen coordenadas basadas en las medidas
enfrente = medidas['Enfrente'] # Medida frontal
atras = medidas['Atras'] # Medida trasera
lat_der = medidas['Lateral derecho'] # Medida lateral derecha
lat_izq = medidas['Lateral izquierda'] # Medida lateral izquierda

# Definición de puntos clave
vertices_principal_unidad = [(0, 0), (enfrente, 0), (atras, lat_der), (0, lat_izq)] # Puntos principales para delimitar perimetro del edificio académico
Vertices_secundarios_unidad = [(-10, -10), (enfrente + 10, -10), (atras + 10, lat_der + 10), (-10, lat_izq + 10)] # Puntos secundarios para delimitar perimetro del terreno de la unidad académica
puntos_pet = [(enfrente * 0.15, lat_izq *-0.02), (enfrente * 0.65, lat_der * 1.02)] # Puntos PET
puntos_HDPE = [(enfrente * 0.85, lat_der *-0.02),(enfrente * 0.40, lat_izq * 1.02)] # Puntos HDPE
Laboratorio_zona = ((enfrente * 0.50, lat_der * 0.85)) # Zona de personas (Laboratorio)
Cafeteria_zona = ((enfrente * 0.35, lat_izq * 0.60))   # Zona de personas (Cafetería)
biblioteca_zona = ((enfrente * 0.65, lat_der * 0.60))  # Zona de personas (Biblioteca)
centro_principal_zona = ((enfrente * 0.50, lat_izq * 0.30)) # Zona de personas (Centro principal)

# Configuración de la visualización
fig, ax = plt.subplots(figsize=(6, 8)) # Tamaño de la figura
terreno = patches.Polygon(vertices_principal_unidad, closed=True, facecolor="#ffffff", edgecolor="#000000", lw=2) # Polígono del terreno
terreno_secundario = patches.Polygon(Vertices_secundarios_unidad, closed=True, facecolor="#ffffff", edgecolor="#AA1C1C", lw=2, linestyle='-', alpha=0.8) # Polígono secundario del terreno
ax.add_patch(terreno_secundario) # Añadir el polígono secundario
ax.add_patch(terreno) # Añadir el polígono del terreno

# Graficar puntos PET
for punto in puntos_pet:
    ax.plot(punto[0], punto[1], 'o', color="#3b1269", markersize=10) # Puntos PET
    ax.text(punto[0] + 1, punto[1], 'PET', fontsize=12, verticalalignment='center', color="#3b1269") # Etiqueta PET

# Graficar puntos HDPE
for punto in puntos_HDPE:
    ax.plot(punto[0], punto[1], 'o', color='#3b1269', markersize=10) # Puntos HDPE
    ax.text(punto[0] + 1, punto[1], 'HDPE', fontsize=12, verticalalignment='center', color='#3b1269') # Etiqueta HDPE

# Graficar zonas de personas
ax.plot(Laboratorio_zona[0], Laboratorio_zona[1], 's', color="#1c6ad1", markersize=10) # Zona Laboratorio
ax.text(Laboratorio_zona[0] + 1, Laboratorio_zona[1], 'Laboratorio', fontsize=12, verticalalignment='bottom', color='#1c6ad1') # Etiqueta Laboratorio
ax.plot(Cafeteria_zona[0], Cafeteria_zona[1], 's', color='#1c6ad1', markersize=10) # Zona Cafetería
ax.text(Cafeteria_zona[0] + 1, Cafeteria_zona[1], 'Cafetería', fontsize=12, verticalalignment='bottom', color='#1c6ad1') # Etiqueta Cafetería
ax.plot(biblioteca_zona[0], biblioteca_zona[1], 's', color='#1c6ad1', markersize=10) # Zona Biblioteca
ax.text(biblioteca_zona[0] + 1, biblioteca_zona[1], 'Biblioteca', fontsize=12, verticalalignment='top', color='#1c6ad1') # Etiqueta Biblioteca
ax.plot(centro_principal_zona[0], centro_principal_zona[1], 's', color='#1c6ad1', markersize=10) # Zona Centro principal
ax.text(centro_principal_zona[0] + 1, centro_principal_zona[1], 'Centro Principal', fontsize=12, verticalalignment='top', color='#1c6ad1') # Etiqueta Centro principal

# Ajustes finales de la gráfica
ax.set_xlim(-20, enfrente + 20) # Límites del eje X
ax.set_ylim(-15, max(lat_der, lat_izq) + 15) # Límites del eje Y
ax.set_aspect('equal') # Proporción igual
plt.title(f"Dimensiones de la unidad académica", pad=20, fontsize=14, fontweight='bold') # Título
plt.grid(True, linestyle=':', alpha=0.6) # Cuadrícula
plt.xlabel('Metros (X)') # Etiqueta eje X
plt.ylabel('Metros (Y)') # Etiqueta eje Y
plt.tight_layout() # Ajustar el diseño para evitar recortes
# Guardar la gráfica
nombre_img = "Grafica_Puntos_PET.png" # Nombre del archivo de la imagen
plt.savefig(os.path.join(carpeta_destino, nombre_img), dpi=400, bbox_inches='tight') # Guardar la imagen
    
plt.show() # Mostrar la gráfica