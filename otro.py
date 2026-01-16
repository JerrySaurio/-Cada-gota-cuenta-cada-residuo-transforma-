import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN DEL DASHBOARD
st.set_page_config(page_title="Dashboard Pluviométrico", layout="wide")
st.title("📊 Sistema de Análisis de Lluvia Máxima")

# 2. CARGA Y FILTRO DE DATOS
@st.cache_data # Esto hace que el dashboard sea ultra fluido
def cargar_datos():
    return pd.read_csv('Datos_Mensuales_mm_validados.csv')

df = cargar_datos()

# 3. MENÚ LATERAL (Sidebar)
st.sidebar.header("Opciones de Visualización")
opcion = st.sidebar.selectbox("Selecciona la estadística a visualizar:", 
                               ['Resumen General', 'Comparativa por Años', 'Exportar para Scala'])

# 4. PROCESO DE CÁLCULO PARA SCALA
# Scala suele trabajar muy bien con archivos Parquet o CSV limpios sin cabeceras extra
if opcion == 'Exportar para Scala':
    st.subheader("⚙️ Preparación de datos para Procesamiento Externo (Scala/Spark)")
    
    # Preparamos un DataFrame optimizado (solo números)
    df_scala = df[df['AÑO'].apply(lambda x: str(x).isdigit())].copy()
    
    st.write("Datos normalizados listos para cálculo de alta intensidad:")
    st.dataframe(df_scala.head())
    
    # Botón para descargar
    csv = df_scala.to_csv(index=False).encode('utf-8')
    st.download_button("Descargar CSV para Scala", data=csv, file_name="datos_para_scala.csv")

# 5. GRÁFICA INTERACTIVA (Fluidez total)
elif opcion == 'Resumen General':
    st.subheader("Análisis de Máximas, Medias y Mínimas")
    
    # Filtrar solo las filas de texto al final para la gráfica
    stats_df = df[df['AÑO'].isin(['MÁXIMA', 'MEDIA', 'MÍNIMA'])]
    
    # Usamos Plotly dentro de Streamlit para el hover fluido
    fig = px.line(stats_df.melt(id_vars='AÑO', var_name='Mes', value_name='Precipitación'), 
                  x='Mes', y='Precipitación', color='AÑO', markers=True,
                  title="Comportamiento Estacional")
    
    st.plotly_chart(fig, use_container_width=True)