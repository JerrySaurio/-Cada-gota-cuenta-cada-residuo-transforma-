import pandas as pd
import numpy as np

# Carga de datos
df_mm_anual =pd.read_csv('Datos_Dia_mm_validados.csv') # Lluvia maxima 
df_Co = pd.read_csv('Coeficiente.csv') # Coeficiente de escorrentia de acuerdo al material del techo
df_medidas = pd.read_csv('Medidas_unidad_academica.csv') # Medidas de la unidad academica

materiales = ["PET suficiente", "Canaletas", "Filtro primario (malla o tela)", "Tubo de bajada",
    "Filtro secundario (arena, grava, carbón)", "Depósito para almacenamiento", "Llave de salida", "Tornillos, alambre, cinta", "Manguera"
] # Lista de materiales
pasos_scall = ["Colocar una canaleta en el borde del techo para recolectar el agua de la lluvia", "Conectar la canaleta a un tubo o embudo inicial que dirija el agua hacia la pared", "Fijar botellas PET cortadas (en forma de canal o media caña) a lo largo de la pared, formando una bajada continua",
    "Unir las botellas con cinta resistente, tornillos o alambre, sobre una estructura de soporte (rejilla, madera reciclada", "Al final del canal, instalar un filtro casero con capas de grava, arena y carbón activado dentro de una botella cortada", "El agua filtrada cae directamente en un tinaco o depósito reciclado con tapa y válvula de salida."
] # Pasos a seguir para la construcción del SCALL
activado = ("El agua de lluvia es dirigida desde el techo a través de las canaletas hacia las botellas PET ensambladas en la pared.\n"
            "El agua pasa por el filtro primario que retiene hojas y residuos grandes.\n"
            "El agua continúa su camino a través del tubo de bajada hacia el filtro secundario que purifica el agua.\n"      
            "¡Genial! ¡El agua limpia se almacena en el deposito listo para su uso!\n\n"
            "El agua recolectada se podria usar para:\n"
            "Riego de plantas, Limpeza de salones y patio, Uso sanitario\n\n"
            "Se debe dar mantenimiento al sistema; monitorearlo, limpiarlo, cambiar filtros, etc\n"
            '"Condicion sana, buena eficiencia"')
# Procedimiento para el calculo de area y perimetro
medidas = dict(zip(df_medidas['Medidas'], df_medidas['Metros'])) # Convertimos a diccionario para fácil acceso
enfrente, atras = medidas['Enfrente'], medidas['Atras'] # Se definen coordenadas basadas en las medidas
lat_der, lat_izq = medidas['Lateral derecho'], medidas['Lateral izquierda'] # Se definen coordenadas basadas en las medidas

# Cálculo de área (Polígono)
vertices = [(0, 0), (enfrente, 0), (atras, lat_der), (0, lat_izq)] # Proyectamos los puntos
x = [v[0] for v in vertices]
y = [v[1] for v in vertices]
area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1))) # Fórmula del área del polígono
perimetro = enfrente + lat_der + atras + lat_izq # Cálculo del perímetro

# Extracción del coeficiente de escorrentia
material_interes = "Techos impermeabilizados o cubiertos con materiales duros (p. ej. Tejas)"
Co = df_Co.loc[df_Co['Material o tipo de construcción'] == material_interes, 'Kc'].item()

# Extracción de mm máxima
columna_a_extraer = 'PROMEDIO'
try:
    mm_maxima_seleccionado = df_mm_anual.loc[df_mm_anual['AÑO'] == 'MÁXIMA', columna_a_extraer].item()
except KeyError:
    print(f"Error: La columna '{columna_a_extraer}' no existe en el archivo.")
    mm_maxima_seleccionado = 0

# Convertimos la columna AÑO a string por seguridad y quitamos espacios en blanco
df_mm_anual['AÑO'] = df_mm_anual['AÑO'].astype(str).str.strip()
fila_maxima = df_mm_anual[df_mm_anual['AÑO'] == 'MÁXIMA'].copy()
reporte = fila_maxima.set_index('AÑO').rename_axis('', axis=0).T # .rename_axis('Datos', axis=1) cambia el nombre que aparece sobre las columnas

# Cálculo de Volumen
mm_maxima = mm_maxima_seleccionado / 1000 # Convertir mm a m3
volumen_captable = area * mm_maxima * Co # m3 volumen utilizable de agua pluvial sin descarte

# Descarte de seguridad (5mm)
volumen_descarte = (5 / 1000) * area * Co
volumen_neto = max(0, volumen_captable - volumen_descarte)

def calcular_volumen_captable(porcentaje_area):
    """Calcula el volumen basado en el porcentaje de superficie."""
    area_seleccionada = area * (porcentaje_area / 100)
    volumen = area_seleccionada * mm_maxima * Co
    return area_seleccionada, volumen

def calcular_capacidad_almacenamiento(tipo_botella, cantidad):
    """Determina la capacidad en litros y m3 según el PET recolectado."""
    capacidad_unitaria = 2.75 if tipo_botella == "1" else 3.0
    total_litros = cantidad * capacidad_unitaria
    return total_litros, total_litros / 1000
        
# Generador de listas formateadas
def generar_lista(titulo, lista):
    salida = []
    salida.append("-" * 60)
    salida.append(f"{titulo}")
    salida.append("-" * 60)

    for i, item in enumerate(lista, start=1):
        salida.append(f"{i}. {item}")

    return "\n".join(salida)

texto_materiales = generar_lista("Materiales para el sistema SCALL", materiales)
texto_pasos = generar_lista("Pasos de contrucción SCALL", pasos_scall)


df_mt = pd.DataFrame(materiales, columns=["Material"]) # Creamos el DataFrame
df_mt.index = df_mt.index + 1 # Ajustamos el índice para que empiece en 1 y no en 0
list_materiales = df_mt.to_string(justify='left')
df_pasos = pd.DataFrame(pasos_scall, columns=["Pasos a seguir"]) # Creamos el DataFrame
df_pasos.index = df_pasos.index + 1 # Ajustamos el índice para que empiece en 1 y no en 0
pasos_seguir = df_pasos.to_string(justify='left')

for i, row in df_mt.iterrows():
    print(f"{i}. {row['Material']}")


# Reporte final
print("-" * 30)
print(reporte)
print("-" * 30)
print(f"Perimetro: {perimetro:.2f} m \nÁrea: {area:.3f} m²")
print(f"Volumen captable: {volumen_captable:.2f} m³\nVolumen final con descarte: {volumen_neto:.2f} m³")

# Guardar reporte
guardar_maxima = df_mm_anual[df_mm_anual['AÑO'] == 'MÁXIMA'].squeeze() # Usamos squeeze() para convertir el DataFrame de 1 fila en una Serie
guardar_maxima.to_csv('Datos_maxima_nuevo.csv', header=False) # Guardar como nueva tabla
