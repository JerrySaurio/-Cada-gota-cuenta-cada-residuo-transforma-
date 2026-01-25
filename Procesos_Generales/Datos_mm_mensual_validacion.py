# Script para limpiar y transformar datos de lluvias mensuales de Chalco, Estado de México.
import pandas as pd

df = pd.read_csv('Datos_Mensuales_mm.csv') # Cargar los datos desde el archivo
print("\nDatos faltantes:") 
print(df.isnull().sum()) # Verificar valores faltantes por columna

# Diccionario para nombres completos de los meses (Abreviado: Completo)
nombres_completos = {
    'ENE': 'ENERO', 'FEB': 'FEBRERO', 'MAR': 'MARZO', 
    'ABR': 'ABRIL', 'MAY': 'MAYO', 'JUN': 'JUNIO', 
    'JUL': 'JULIO', 'AGO': 'AGOSTO', 'SEP': 'SEPTIEMBRE', 
    'OCT': 'OCTUBRE', 'NOV': 'NOVIEMBRE', 'DIC': 'DICIEMBRE'
}
cambio_nombre_columnas = { 'ACUM': 'ACUMULACION (mm)', 'PROM': 'PROMEDIO' } # Cambios de nombres para columnas adicionales

meses_abrev = list(nombres_completos.keys()) # Lista de abreviaciones de meses

for mes in meses_abrev: # Convertir las columnas de meses a tipo numérico y rellenar NaN con 0
    df[mes] = pd.to_numeric(df[mes], errors='coerce') # Convertir a float después de rellenar NaN con 0

es_año = pd.to_numeric(df['AÑO'], errors='coerce').notnull().copy() # Filtrar solo filas con años numéricos

# Calcular los valores estadísticos por columna .min(), .max(), .mean(), .std(), .count()
# Insertar estos valores en las filas correspondientes al final del archivo
df.loc[df['AÑO'] == 'MÁXIMA', meses_abrev] = df.loc[es_año, meses_abrev].max().values # Valores máximos por mes
df.loc[df['AÑO'] == 'MÍNIMA', meses_abrev] = df.loc[es_año, meses_abrev].min().values # Valores mínimos por mes
df.loc[df['AÑO'] == 'MEDIA', meses_abrev] = df.loc[es_año, meses_abrev].mean().round(1).values # Valores medios por mes
df.loc[df['AÑO'] == 'DESV.ST', meses_abrev] = df.loc[es_año, meses_abrev].std().round(1).values # Desviación estándar por mes
conteo_meses = (df.loc[es_año, meses_abrev] >= 0).sum(axis=1) # Contar meses con datos por año
df.loc[es_año, 'MESES'] = conteo_meses.values # Agregar columna 'MESES' al DataFrame

# Calcular columnas adicionales ACUM y PROM
df.loc[es_año, 'ACUM'] = df.loc[es_año, meses_abrev].sum(axis=1).round(2) # Suma acumulada por año
df.loc[es_año, 'PROM'] = (df.loc[es_año, 'ACUM'] / conteo_meses).round(1) # Promedio anual por año

# Modificar el DataFrame final
df.drop(columns=['MESES'], inplace=True) # Eliminar columna 'MESES' si existe
df[meses_abrev] = df[meses_abrev].fillna(0).astype(float).round(2) # Rellenar NaN con 0 y convertir a float con 2 decimales
df.rename(columns=nombres_completos, inplace=True) # Renombrar columnas de meses
df.rename(columns=cambio_nombre_columnas, inplace=True) # Cambiar nombres de las columnas ACUM y PROM
meses_nuevos = list(nombres_completos.values()) # Actualizar las filas de estadísticas al final con los nuevos nombres de meses

# Mostrar los datos transformados y guardar los datos limpios en un nuevo archivo CSV
Nuevo_archivo = 'Datos_Mensuales_mm_validados.csv'
df.to_csv(Nuevo_archivo, index=False)
print(f"\nDatos limpios y guardados en {Nuevo_archivo}")
print("Datos transformados.")