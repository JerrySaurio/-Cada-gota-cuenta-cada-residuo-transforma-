import pandas as pd
import numpy as np

# Carga de datos
df_mm_anual =pd.read_csv('Datos_Dia_mm_validados.csv') # Lluvia maxima 
df_Co = pd.read_csv('Coeficiente.csv') # Coeficiente de escorrentia de acuerdo al material del techo
df_medidas = pd.read_csv('Medidas_unidad_academica.csv') # Medidas de la unidad academica

# --- Procedimiento para el calculo de area y perimetro ---
medidas = dict(zip(df_medidas['Medidas'], df_medidas['Metros'])) # Convertimos a diccionario para fácil acceso
enfrente, atras = medidas['Enfrente'], medidas['Atras'] # Se definen coordenadas basadas en las medidas
lat_der, lat_izq = medidas['Lateral derecho'], medidas['Lateral izquierda'] # Se definen coordenadas basadas en las medidas

# Cálculo de área (Polígono)
vertices = [(0, 0), (enfrente, 0), (atras, lat_der), (0, lat_izq)] # Proyectamos los puntos
x = [v[0] for v in vertices]
y = [v[1] for v in vertices]
area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1))) # Fórmula del área del polígono
perimetro = enfrente + lat_der + atras + lat_izq # Cálculo del perímetro
print(f"Perimetro: {perimetro:.2f} m \nÁrea: {area:.3f} m²")

# --- Extracción del coeficiente de escorrentia ----
material_interes = "Techos impermeabilizados o cubiertos con materiales duros (p. ej. Tejas)"
Co = df_Co.loc[df_Co['Material o tipo de construcción'] == material_interes, 'Kc'].item()

# --- Extracción de mm máxima ----
# Se extrae la fila MÁXIMA y convertirla en Serie (Lista Vertical)
fila_vertical = df_mm_anual[df_mm_anual['AÑO'] == 'MÁXIMA'].squeeze() # Usamos squeeze() para convertir el DataFrame de 1 fila en una Serie
fila_vertical.to_csv('Datos_maxima_nuevo.csv', header=False) # Guardar como nueva tabla

# Convertimos la columna AÑO a string por seguridad y quitamos espacios en blanco
df_mm_anual['AÑO'] = df_mm_anual['AÑO'].astype(str).str.strip()
fila_maxima = df_mm_anual[df_mm_anual['AÑO'] == 'MÁXIMA'].copy()
reporte = fila_maxima.set_index('AÑO').rename_axis('', axis=0).T # .rename_axis('Datos', axis=1) cambia el nombre que aparece sobre las columnas
print(reporte)

mm_maxima_seleccionado = df_mm_anual.loc[df_mm_anual['AÑO'] == 'MÁXIMA', 'PROMEDIO'].item() # mm seleccionado
mm_anual = mm_maxima_seleccionado / 1000 # Convertir mm a m3
volumen_captable = area * mm_anual * Co # m3 volumen anual utilizable de agua pluvial sin descarte
mm_descarte = 5 / 1000  # Descarte de 5 mm en metros
volumen_descarte_aprox = area * mm_descarte 
volumen_descarte = volumen_descarte_aprox - volumen_captable
print(f"Volumen: {volumen_captable:.2f} m3\nDescarte: {volumen_descarte:.2f}")
