import pandas as pd
import os

archivo_excel = 'Datos_Encuesta.xlsx'
hoja_destino = 'Analisis_Conciencia'

# Aquí definimos qué respuestas se consideran "Conciencia Ambiental" (1) y cuáles No (0).
# Esta es la parte más crítica del análisis de datos: la interpretación.
#Logica en bases a las respuestas
def clasificar_respuesta(numero_pregunta, respuesta):
    respuesta = str(respuesta).lower().strip()
    
    # Lógica por pregunta
    if numero_pregunta == 1: # Escasez de agua
        # Asumimos que percibir la escasez es tener conciencia de la realidad
        if respuesta in ['varias veces al mes/semana', 'algunas veces al año']: return 'Consciente'
        return 'No Consciente' # "Nunca" puede implicar desconexión con la crisis hídrica general
        
    elif numero_pregunta == 2: # Separación de basura
        if respuesta in ['siempre', 'a veces']: return 'Consciente'
        return 'No Consciente'
        
    elif numero_pregunta == 3: # Conocimiento CAAP
        if respuesta in ['si', 'he escuchado sobre ello']: return 'Consciente'
        return 'No Consciente'
        
    elif numero_pregunta == 4: # Usos agua lluvia
        if respuesta in ['riego de planta', 'tareas domesticas']: return 'Consciente'
        return 'No Consciente' # "No utilizaria esa agua"
        
    elif numero_pregunta == 5: # Eficiencia basura
        # Asumimos que ser crítico ("Deficiente") o realista ("Aceptable") muestra interés
        # Si dicen "Eficiente" y el servicio es malo, podría ser falta de criterio, 
        # pero esto es subjetivo. Ajustaremos a:
        if respuesta in ['deficiente', 'aceptable', 'muy deficiente']: return 'Consciente'
        return 'No Consciente' # "Eficiente" (Conformismo) o "Muy eficiente"
        
    elif numero_pregunta == 6: # Participación limpieza
        if respuesta == 'si': return 'Consciente'
        return 'No Consciente'
        
    elif numero_pregunta == 7: # Inversión CAAP
        if respuesta in ['si', 'tal vez']: return 'Consciente'
        return 'No Consciente'
        
    elif numero_pregunta == 8: # Capacitación
        if respuesta == 'si': return 'Consciente'
        return 'No Consciente'
        
    elif numero_pregunta == 9: # Causa Inundaciones
        # Reconocer que la basura es causa (total o parcial) es tener conciencia
        if 'causa' in respuesta and 'otra' not in respuesta: return 'Consciente'
        return 'No Consciente' # "La causa es otra" (Negación)
    
    return 'No Definido'

# Procesamiento
try:
    print("Iniciando análisis de conciencia...")
    
    # Verificamos si existe el archivo (usando datos mock si no)
    if not os.path.exists(archivo_excel):
        print("⚠ Archivo no encontrado. Asegúrate de haber corrido el script anterior primero.")
    
    xl = pd.ExcelFile(archivo_excel)
    resumen_conciencia = []

    for i, nombre_hoja in enumerate(xl.sheet_names):
        # Ignorar hojas que no sean preguntas (como la de 'Resultados' o 'Analisis_Conciencia' si ya existen)
        if "Analisis" in nombre_hoja or "Resultados" in nombre_hoja:
            continue
            
        # Se determina número de pregunta basado en el orden o nombre
        # Asumimos orden secuencial 1 a 9
        num_pregunta = i + 1 
        
        # Lectura y limpieza
        df_full = pd.read_excel(archivo_excel, sheet_name=nombre_hoja, header=None)
        
        try:
            texto_pregunta = str(df_full.iloc[1, 1])
        except:
            texto_pregunta = f"Pregunta {num_pregunta}"
            
        df = df_full.iloc[2:].copy()
        df.columns = ['Respuesta', 'Total']
        df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0).astype(int)
        df = df.dropna(subset=['Respuesta'])
        
        # Cálculos
        total_encuestados = df['Total'].sum()
        consciente_count = 0
        no_consciente_count = 0
        
        for index, row in df.iterrows():
            categoria = clasificar_respuesta(num_pregunta, row['Respuesta'])
            if categoria == 'Consciente':
                consciente_count += row['Total']
            else:
                no_consciente_count += row['Total']
        
        # Evitar división por cero
        if total_encuestados == 0:
            porc_consciente = 0
            porc_no_consciente = 0
        else:
            porc_consciente = (consciente_count / total_encuestados) * 100
            porc_no_consciente = (no_consciente_count / total_encuestados) * 100
            
        resumen_conciencia.append({
            "No.": num_pregunta,
            "Pregunta": texto_pregunta,
            "Total Encuestados": total_encuestados,
            "Votos Conscientes": consciente_count,
            "Votos No Conscientes": no_consciente_count,
            "% Conciencia": round(porc_consciente, 2),
            "% No Consciente": round(porc_no_consciente, 2),
            "Interpretación": "Alta Conciencia" if porc_consciente > 50 else "Baja Conciencia"
        })

    # Crear DataFrame final
    df_analisis = pd.DataFrame(resumen_conciencia)
    
    # Exportacion
    # Usamos openpyxl para agregar la hoja sin borrar las anteriores
    with pd.ExcelWriter(archivo_excel, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df_analisis.to_excel(writer, sheet_name=hoja_destino, index=False)
        
    print(f"\nÉxito: Se ha creado la hoja '{hoja_destino}' en '{archivo_excel}'.")
    print("\nVista previa de los resultados:")
    print(df_analisis[['No.', '% Conciencia', '% No Consciente', 'Interpretación']].to_string(index=False))

except Exception as e:
    print(f"Error en el proceso: {e}")
    import traceback
    traceback.print_exc()