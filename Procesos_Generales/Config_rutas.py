# config_rutas.py
import os

# CONFIGURACIÓN GLOBAL DE RUTAS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Carpeta raíz del proyecto (donde está este archivo)

# Carpetas principales
CARPETA_DATOS = os.path.join(BASE_DIR, "Datos_recopilados")
CARPETA_RESULTADOS = os.path.join(BASE_DIR, "SCALL_Resultados")
CARPETA_GRAFICAS = os.path.join(BASE_DIR, "Graficas_Datos_Generales")

# Crear carpetas si no existen
os.makedirs(CARPETA_RESULTADOS, exist_ok=True)
os.makedirs(CARPETA_GRAFICAS, exist_ok=True)
