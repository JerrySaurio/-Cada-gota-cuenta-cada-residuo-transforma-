import pandas as pd
import matplotlib.pyplot as plt
import os

carpeta_destino = 'Graficas_Datos_Generales'
# Crear carpeta si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

df = pd.read_csv('Datos_Dia_mm_validados.csv') # Cargar los datos limpios y verificados desde el archivo

# Preparar los datos para la gráfica de máximas, medias y mínimas mensuales
meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO',
         'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']

# Usamos .set_index('AÑO') para que sea más fácil localizar las filas por nombre
df_stats = df.set_index('AÑO')

# Extraemos los valores de las filas de estadísticas
Maxima = df_stats.loc['MÁXIMA', meses]
Minima = df_stats.loc['MÍNIMA', meses]
Media = df_stats.loc['MEDIA', meses]
meses_etiquetas = [mes.capitalize() for mes in meses] # Etiquetas con la primera letra en mayúscula

# Se crea la gráfica de líneas para Máxima, Media y Mínima
plt.figure(figsize=(12, 6)) # Tamaño de la figura
plt.rcParams['axes.facecolor'] = "#fdfdfdef" # Fondo ligeramente gris para resaltar líneas

# Dibujamos las líneas con estilos personalizados
plt.plot(meses_etiquetas, Maxima, label='Máxima', marker='o', color= "#AC0A0A", linewidth=2, zorder=2)
plt.plot(meses_etiquetas, Media, label='Media', marker='s', color= "#0D995F", linestyle='--', linewidth=2.5, zorder=2)
plt.plot(meses_etiquetas, Minima, label='Mínima', marker='v', color="#005F85", linewidth=2, zorder=3)

# Función para evitar que los números se encimen
for i in range(len(meses_etiquetas)): # Iterar sobre cada mes
    # Valor de Máxima (arriba del punto) 
    plt.text(i, Maxima[i] + (Maxima.max()*0.02), f'{Maxima[i]:.1f}',
             ha='left', va='bottom', color='#AC0A0A', fontweight='bold', fontsize=9, bbox=dict(facecolor='#fdfdfdef', edgecolor='none', pad=0.5))
    # Valor de Media (arriba del punto)
    plt.text(i, Media[i] + (Maxima.max()*0.02), f'{Media[i]:.1f}', 
             ha='center', va='bottom', color='#0D995F', fontweight='bold', fontsize=9)
    # Valor de Mínima (Solo si es > 0)
    if Minima[i] > 0.01:
        plt.text(i, Minima[i] - (Maxima.max()*0.03), f'{Minima[i]:.1f}', 
                 ha='center', va='top', color='#005F85', fontweight='bold', fontsize=9)
    
# Configuración visual de la gráfica
ax = plt.gca() # Obtener el eje actual
ax.tick_params(axis='y', length=0) # Quitar las marcas de las ticks del eje Y
ax.tick_params(axis='x', length=6, pad=1) # Aumentar la longitud de las ticks del eje X
ax.grid(False) # Quitar la cuadrícula por defecto
ax.grid(axis='y', color="#969696FF", linestyle='--', alpha=0.5, zorder=0) # Líneas de la cuadrícula horizontales
ax.spines[['top','left', 'bottom','right']].set_visible(False) # Quitar los bordes de la gráfica
plt.suptitle('Precipitación Máxima en 24 horas en la Zona de Chalco (1961-2025)', fontsize=16, fontweight='bold') # Título de la gráfica
plt.title('Valores Mínimos, Medios y Máximos', fontsize=10, fontweight='bold', pad=15, color='gray') # Subtítulo de la gráfica
plt.ylabel('Precipitación (mm)', fontsize=13, labelpad=10) # Etiqueta del eje Y
plt.xlabel('Meses', fontsize=13, labelpad=10) # Etiqueta del eje X
plt.subplots_adjust(bottom=0.15, top=0.85) # Ajuste de los márgenes superior e inferior
plt.xticks(rotation=30, fontsize=11, ha='right') # Rotación de las etiquetas del eje X
plt.yticks(fontsize=11) # Tamaño de las etiquetas del eje Y
plt.legend(loc='upper right', frameon=True, shadow=True, fontsize=12) # Leyenda de la gráfica

# Ajustar el límite de Y para que los textos no se corten
plt.ylim(Minima.min() - 5, Maxima.max() + (Maxima.max()*0.15)) # Margen superior e inferior
plt.tight_layout()
# Guardar la gráfica
nombre_img = "Grafica_estadisticas_lluvia_24h.png" # Nombre del archivo de la imagen
plt.savefig(os.path.join(carpeta_destino, nombre_img), dpi=400, bbox_inches='tight') # Guardar la imagen
   
plt.show()