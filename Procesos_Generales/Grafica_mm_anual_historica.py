# Grafica_mm_anual_historica.py
import pandas as pd
import matplotlib.pyplot as plt
import os
def Datos_Mensuales():
    carpeta_destino = 'Graficas_Datos_Generales'
    # Crear carpeta si no existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    df = pd.read_csv('Datos_Mensuales_mm_validados.csv') # Cargar datos

    # Filtrar y limpiar
    # Convertimos AÑO a string para que Matplotlib lo trate como etiqueta y no como escala numérica
    df_anual = df[pd.to_numeric(df['AÑO'], errors='coerce').notnull()].copy() # Filtrar filas con años numéricos
    df_anual['AÑO_STR'] = df_anual['AÑO'].astype(str) # Nueva columna para etiquetas

    # Configurar la figura
    plt.figure(figsize=(14, 7)) # Tamaño de la figura
    plt.rcParams['axes.facecolor'] = "#fdfdfdef" # Fondo ligeramente gris para resaltar barras

    # Crear la gráfica de barras
    # Al usar 'AÑO_STR', Python los pega uno tras otro sin dejar huecos por números faltantes
    columna_datos = 'ACUMULACION (mm)' # Columna con los datos de precipitación anual
    bars = plt.bar(df_anual['AÑO_STR'], df_anual[columna_datos], color='#00CCFF', zorder=3) # Barras azules

    # Etiquetas de valor (verticales)
    for bar in bars: # Iterar sobre cada barra
        yval = bar.get_height() # Altura de la barra
        if yval > 0: # Solo si el valor es mayor que 0
            plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval:.0f}', 
                     va='bottom', ha='center', rotation=90, fontsize=7, color='#444444') # Etiqueta encima de la barra

    # Configuración visual
    ax = plt.gca() # Obtener el eje actual
    ax.spines[['top', 'right', 'left']].set_visible(False) # Quitar bordes innecesarios
    ax.grid(axis='y', linestyle='--', alpha=0.4, color='#969696FF', zorder=0) # Líneas de cuadrícula horizontales
    ax.grid(axis='x', visible=False) # Quitar líneas verticales

    # Configurar Ejes
    plt.title('Promedio de precipitación anual histórica zona Chalco (MM)', fontsize=16, fontweight='bold', pad=25) # Título
    plt.ylabel('Precipitación (mm)', fontsize=12) # Etiqueta del eje Y
    plt.xlabel('Año', fontsize=12) # Etiqueta del eje X
    plt.xticks(rotation=90, fontsize=8) # Rotar etiquetas del eje X
    plt.ylim(0, df_anual[columna_datos].max() * 1.15) # Ajustar límites de Y para que quepan los números

    # Ajuste final
    plt.tight_layout() # Ajustar el diseño para evitar recortes
    
    plt.figtext(0.5, 0.01, "* El año 2013 no cuenta con registros verificados.", 
                ha="center", fontsize=8, color="red", style='italic') # Nota al pie
    
    # Guardar la gráfica
    nombre_img = "Grafica_mm_anual_historica.png" # Nombre del archivo de la imagen
    plt.savefig(os.path.join(carpeta_destino, nombre_img), dpi=400, bbox_inches='tight') # Guardar la imagen
    
    plt.show() # Mostrar la gráfica
Datos_Mensuales()