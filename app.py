import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Título y configuración de la app
st.title("💧 Proyecto de Captación Pluvial")
st.subheader("Gestión de Inventario y Materiales")

# 2. Tus datos (Limpios y estructurados)
raw_material = [
    "PET suficiente", "Canaletas", "Filtro primario (malla o tela)",
    "Tubo de bajada", "Filtro secundario (arena, grava, carbón)",
    "Depósito para almacenamiento", "Llave de salida",
    "Tornillos, alambre, cinta", "Manguera"
]

# Creamos el DataFrame
df = pd.DataFrame(raw_material, columns=["Materiales Requeridos"])
df.index = df.index + 1

# 3. Visualización en Streamlit
# Mostramos la tabla interactiva (pueden ordenarla, ampliarla, etc.)
st.write("### Listado Oficial")
st.dataframe(df, use_container_width=True)

# 4. Un toque extra de "App": Checkboxes interactivos
st.write("---")
st.write("### Verificación de Campo")
for item in raw_material:
    st.checkbox(f"Tengo: {item}")
    