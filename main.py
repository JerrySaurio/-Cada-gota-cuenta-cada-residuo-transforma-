# Importar librerias
import pandas as pd
import matplotlib.pyplot as plt
import os
from Grafica_mm_anual_historica import Datos_Mensuales

carpeta_destino = 'Graficas_Datos_Generales'
# Crear carpeta si no existe
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)
    
print("Completado {Datos_Mensuales}")