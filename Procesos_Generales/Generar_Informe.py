from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import cm
import os
from Config_rutas import CARPETA_RESULTADOS, CARPETA_GRAFICAS

def generar_informe():
    nombre_pdf = os.path.join(CARPETA_RESULTADOS, "Informe_Final_SCALL.pdf")

    doc = SimpleDocTemplate(nombre_pdf, pagesize=letter)
    estilos = getSampleStyleSheet()
    estilos.add(ParagraphStyle(name="Titulo", parent=estilos["Title"], alignment=TA_CENTER))
    estilos.add(ParagraphStyle(name="Justificado", parent=estilos["Normal"], alignment=TA_JUSTIFY))

    story = []

    # ---- PORTADA ----
    story.append(Paragraph("Captación de agua pluvial y gestión de residuos.", estilos["Titulo"]))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph('"Cada gota cuenta cada residuo transforma"', estilos["Heading2"]))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("Universidad Nacional Rosario Castellanos", estilos["Normal"]))
    story.append(PageBreak())

    # ---------- RESUMEN ----------
    story.append(Paragraph("Resumen Ejecutivo", estilos["Heading1"]))
    story.append(Spacer(1, 0.4*cm))

    resumen_texto = """
El municipio de Chalco enfrenta problemáticas recurrentes de inundaciones, escasez de agua potable 
y acumulación de residuos plásticos. Ante este contexto, el presente proyecto desarrolla el Sistema 
de Captación de Agua Pluvial y Gestión de Residuos Plásticos (SCALL) en la Unidad Académica de la 
Universidad Nacional Rosario Castellanos como una propuesta sustentable, educativa y replicable.

Mediante el análisis de datos climatológicos históricos y la determinación geométrica de la superficie 
disponible, se estimó el potencial de captación de agua de lluvia y se dimensionó un sistema piloto 
basado en la reutilización de botellas PET como estructura de conducción y almacenamiento.

En síntesis, SCALL transforma la lluvia en recurso y los residuos en infraestructura, fortaleciendo 
la resiliencia hídrica y la conciencia ambiental en el entorno universitario.
"""
    story.append(Paragraph(resumen_texto, estilos["Justificado"]))
    story.append(PageBreak())

    # ---- LISTA DE GRÁFICAS ----
    graficas = [
        ("Lluvia Máxima 24 horas", "Grafica_estadisticas_lluvia_24h.png"),
        ("Lluvia Máxima Mensual", "Grafica_estadisticas_lluvia_mensual.png"),
        ("Histórico de Precipitación", "Grafica_mm_anual_historica.png"),
    ]

    for titulo, archivo in graficas:
        story.append(Paragraph(titulo, estilos["Heading2"]))
        story.append(Spacer(1, 0.3*cm))

        ruta_img = os.path.join(CARPETA_GRAFICAS, archivo)

        if os.path.exists(ruta_img):
            img = Image(ruta_img)
            img.drawWidth = 17 * cm
            img.drawHeight = 11 * cm
            story.append(img)

        else:
            story.append(Paragraph(f"Imagen no encontrada: {archivo}", estilos["Normal"]))

        story.append(PageBreak())

    # Insertar gráfica con diferente altura
    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_Perimetro_Area.png")
    if os.path.exists(ruta_img):
        story.append(Image(ruta_img, width=14*cm, height=18*cm))
        story.append(Spacer(1, 0.5*cm))
    else:
        story.append(Paragraph("Gráfica no encontrada.", estilos["Normal"]))

    # Texto final
    story.append(Paragraph(
        "El presente informe presenta el cálculo de área y perímetro de la unidad académica "
        "para el diseño del sistema SCALL de captación de agua pluvial.", estilos["Normal"]
    ))

    ruta_img = os.path.join(CARPETA_GRAFICAS, "Grafica_Puntos_PET.png")
    if os.path.exists(ruta_img):
        story.append(Image(ruta_img, width=14*cm, height=18*cm))
        story.append(Spacer(1, 0.5*cm))
    else:
        story.append(Paragraph("Gráfica no encontrada.", estilos["Normal"]))

    # Texto final
    story.append(Paragraph(
        "El presente informe presenta el cálculo de área y perímetro de la unidad académica "
        "para el diseño del sistema SCALL de captación de agua pluvial.", estilos["Normal"]
    ))

    # ---------- CONCLUSIÓN ----------
    story.append(Paragraph("Conclusión General", estilos["Heading1"]))
    story.append(Spacer(1, 0.4*cm))

    conclusion_texto = """
El desarrollo del sistema SCALL demuestra que es posible diseñar soluciones sostenibles integrando 
análisis de datos, modelado geométrico y reutilización de materiales. Los resultados evidencian que 
la Unidad Académica cuenta con un alto potencial de captación de agua pluvial capaz de contribuir al 
abastecimiento para usos no potables.

La propuesta no solo plantea una alternativa técnica viable y de bajo costo, sino que promueve la 
participación activa de la comunidad universitaria en la gestión responsable del agua y los residuos. 
De esta manera, SCALL se proyecta como un modelo replicable en otras instituciones educativas y 
comunidades con condiciones similares.
"""
    story.append(Paragraph(conclusion_texto, estilos["Justificado"]))

    doc.build(story)

if __name__ == "__main__":
    generar_informe()
