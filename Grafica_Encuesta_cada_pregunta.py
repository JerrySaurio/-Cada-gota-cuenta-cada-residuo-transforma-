# Grafica_Encuesta.py
# Este script lee un archivo Excel con datos de encuestas y genera gráficas de pastel para cada pregunta.
import pandas as pd
import matplotlib.pyplot as plt
import os
import textwrap

# Configuración inicial y constantes
archivo_excel = 'Datos_Encuesta.xlsx' # Nombre del archivo Excel con los datos
carpeta_destino = 'Graficas_Encuesta_de_cada_pregunta' # Carpeta donde se guardarán las gráficas
TOTAL_ESPERADO = 44  # Total esperado de respuestas

# Crear carpeta si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

# Procesar cada hoja del archivo Excel
try:
    xl = pd.ExcelFile(archivo_excel) # Cargar el archivo Excel
    
    for nombre_hoja in xl.sheet_names: # Iterar sobre cada hoja
        # Leemos la hoja completa para extraer la pregunta
        df_full = pd.read_excel(archivo_excel, sheet_name=nombre_hoja, header=None) # Leer sin encabezado
        pregunta_completa = str(df_full.iloc[1, 1]) # Extraer la pregunta completa
        pregunta_ajustada = "\n".join(textwrap.wrap(pregunta_completa, width=60)) # Ajustar el texto de la pregunta
        
        # Extraemos los datos (Respuestas y Totales)
        df = df_full.iloc[2:].copy() # Saltar las dos primeras filas
        df.columns = ['Respuesta', 'Total'] # Asignar nombres a las columnas
        df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0).astype(int) # Convertir a numérico y manejar errores
        df = df.dropna(subset=['Respuesta']) # Eliminar filas sin respuesta
        
        respuestas = df['Respuesta'].tolist() # Lista de respuestas
        valores = df['Total'].tolist() # Lista de totales
        suma_actual = sum(valores) # Suma actual de respuestas

        # Crear la gráfica de pastel
        fig, ax = plt.subplots(figsize=(12, 7)) # Tamaño de la figura
        colores = ['#1B262C', '#16476A', '#1D546D', '#5F9598', '#79C9C5', '#F3F4F4'] # Paleta de colores personalizada

        wedges, texts, autotexts = ax.pie( # Crear la gráfica de pastel
            valores, # Datos para la gráfica
            autopct=lambda p: '{:.0f}'.format(p * suma_actual / 100) if p > 0 else '', # Mostrar solo valores mayores a 0
            startangle=140,# Ángulo inicial para mejor visualización
            colors=colores, # Paleta de colores personalizada
            pctdistance=0.75, # Distancia de los porcentajes desde el centro
            wedgeprops=dict(width=0.4, edgecolor='w') # Ancho de las porciones y color del borde
        )

        # Leyenda detallada con ceros
        etiquetas_leyenda = [f"{res}: {val} personas." for res, val in zip(respuestas, valores)] # Incluir ceros en la leyenda
        
        ax.legend(wedges, etiquetas_leyenda, # Etiquetas de la leyenda
                  title=f"Muestra: {suma_actual}/{TOTAL_ESPERADO}", # Título de la leyenda con muestra actual y total esperado
                  loc="center left", # Ajuste de posición de la leyenda
                  bbox_to_anchor=(1, 0, 0.5, 1), # Ajuste de posición de la leyenda
                  fontsize=10) # Ajuste de tamaño de fuente de la leyenda

        # Estilo del título y textos
        plt.title(pregunta_ajustada, fontsize=12, fontweight='bold', pad=2) # Título con la pregunta completa ajustada
        plt.setp(autotexts, size=12, weight="bold", color="white") # Estilo de los textos dentro de la gráfica
        plt.tight_layout() # Ajuste del diseño para evitar recortes

        # Guardar la gráfica
        nombre_img = f"{nombre_hoja.replace(' ', '_')}.png" # Nombre del archivo de la imagen
        plt.savefig(os.path.join(carpeta_destino, nombre_img), dpi=400, bbox_inches='tight') # Guardar la imagen
        
        plt.show() # Mostrar la gráfica
        print(f"✅ Procesada: {nombre_hoja} con su pregunta completa.") # Confirmación de procesamiento

except Exception as e: # Manejo de errores
    print(f"Error: {e}") # Mostrar el error ocurrido