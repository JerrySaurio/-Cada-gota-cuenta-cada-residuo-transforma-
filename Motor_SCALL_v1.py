from Procesos_Generales.Config_rutas import CARPETA_DATOS
import pandas as pd
import numpy as np
import sys
import os

# Carga segura de archivos
def cargar_csv(nombre_archivo):
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)
    try:
        return pd.read_csv(ruta)
    except FileNotFoundError:
        print(f"\nERROR: No se encontró el archivo:\n{ruta}")
        print("Verifica que la carpeta 'Datos_recopilados' exista y contenga el CSV.")
        sys.exit()

df_mm_anual = cargar_csv("Datos_Dia_mm_validados.csv")
df_Co = cargar_csv("Coeficiente.csv")
df_medidas = cargar_csv("Medidas_unidad_academica.csv")

CONFIG = { 
    "material_techo": "Techos impermeabilizados o cubiertos con materiales duros (p. ej. Tejas)",
    "columna_lluvia": "PROMEDIO",
    "mm_descarte": 5
} # Configuración general

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

# Procedimiento para el calculo de area y perimetro con el archivo Medidas_unidad_academica.csv
medidas = dict(zip(df_medidas['Medidas'], df_medidas['Metros'])) # Convertimos a diccionario para fácil acceso
try:
    enfrente, atras = medidas['Enfrente'], medidas['Atras'] # Se definen coordenadas basadas en las medidas
    lat_der, lat_izq = medidas['Lateral derecho'], medidas['Lateral izquierda'] # Se definen coordenadas basadas en las medidas
except KeyError:
    print("ERROR: Medidas incorrectas en archivo de unidad académica")
    sys.exit()

# Cálculo de área (Polígono)
vertices = [(0, 0), (enfrente, 0), (atras, lat_der), (0, lat_izq)] # Proyectamos los puntos
x = [v[0] for v in vertices]
y = [v[1] for v in vertices]
area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1))) # Fórmula del área del polígono
perimetro = enfrente + lat_der + atras + lat_izq # Cálculo del perímetro

# Extracción del coeficiente de escorrentia del archivo Coeficiente.csv
fila_material = df_Co[df_Co['Material o tipo de construcción'] == CONFIG["material_techo"]]
if fila_material.empty:
    print("ERROR: Material de techo no encontrado en Coeficiente.csv")
    sys.exit()
Co = fila_material['Kc'].values[0]

# Extracción de mm máxima con el archivo Datos_Dia_mm_validados.csv
df_mm_anual['AÑO'] = df_mm_anual['AÑO'].astype(str).str.strip()
fila_maxima = df_mm_anual[df_mm_anual['AÑO'] == 'MÁXIMA']
if fila_maxima.empty:
    print("ERROR: Fila 'MÁXIMA' no encontrada en Datos_Dia_mm_validados.csv")
    sys.exit()
mm_maxima = fila_maxima[CONFIG["columna_lluvia"]].values[0] / 1000 # Lluvia máxima

# Cálculo de Volumen
volumen_captable = area * mm_maxima * Co # m3 volumen utilizable de agua pluvial sin descarte

# Funcion que calcula el volumen basado en el porcentaje de superficie
def calcular_volumen_captable(porcentaje_area):
    area_seleccionada = area * (porcentaje_area / 100)
    volumen = area_seleccionada * mm_maxima * Co
    return area_seleccionada, volumen

# Determina la capacidad en litros y m3 según el PET recolectado.
def calcular_capacidad_almacenamiento(tipo_botella, cantidad):
    capacidad_unitaria = 2.5 if tipo_botella == "1" else 3.0
    total_litros = cantidad * capacidad_unitaria
    return total_litros, total_litros / 1000

# Calcula el impacto del primer descarte de 5mm.
def calcular_descarte(area_captada, volumen_sin_descarte):
    volumen_descarte = area_captada * (5/1000)
    utilizable = volumen_sin_descarte - volumen_descarte
    return max(0, utilizable) # Si el descarte supera al volumen, no devuelva negativo.

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
