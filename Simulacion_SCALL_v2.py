from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import Motor_SCALL_v1 as MtSll
import os

CARPETA_RESULTADOS = "SCALL_Resultados"

if not os.path.exists(CARPETA_RESULTADOS):
    os.makedirs(CARPETA_RESULTADOS)

CONFIG_UI = {
    "nombre_proyecto": 'Captación de agua pluvial y gestión de residuos.\n"Cada gota cuenta cada residuo transforma"',
    "institucion": "Universidad Nacional Rosario Castellanos",
    "autor": 'Equipo 3',
}

def bienvenida():
    print("\n" + "="*60)
    print("Bienvenid@ al sistema SCALL — Captación de Agua Pluvial UNRC")
    print("Este sistema transforma reciclaje PET en solución sustentable.")
    print("="*60)
    print(MtSll.texto_materiales)
    print("\nVerificando materiales disponibles...\n")

def preguntar_si_no(mensaje):
    while True:
        resp = input(mensaje).strip().lower()
        if resp in ("si", "no"):
            return resp
        print("Respuesta inválida. Solo 'si' o 'no'.")

def verificacion():
    if preguntar_si_no("¿Cuentas con todos los materiales? (Si/No): ") == "no":
        print("Sin materiales no hay sistema SCALL.")
        return False

    print("\n¡Genial! ¡Tienes todos los materiales necesarios!\n")
    print(MtSll.texto_pasos)

    if preguntar_si_no("\n¿Sistema SCALL construido exitosamente? (Si/No): ") == "no":
        print("Sistema no construido. Sin infraestructura no hay sistema de captacion pluvial.\nProceso finalizado.")
        return False

    print("\n¡Genial! ¡Tienes un sistema de captación de agua pluvial listo para operar!")
    return True

def seleccionar_porcentaje():
    while True:
        try:
            porcentaje = float(input("Ingrese porcentaje de área a captar (0-100): "))
            if 0 < porcentaje <= 100:
                return porcentaje
        except:
            pass
        print("Valor inválido. Intente nuevamente.")

def seleccionar_botellas():
    while True:
        tipo = input("Seleccione tipo de botella (1 = 2.5L | 2 = 3L): ")
        if tipo in ("1", "2"):
            try:
                cantidad = int(input("Cantidad de botellas interconectadas: "))
                if cantidad > 0:
                    return tipo, cantidad
            except:
                pass
        print("Datos inválidos. Intente nuevamente.")

def generar_reporte(datos):
    nombre_archivo = os.path.join(CARPETA_RESULTADOS, "Reporte_SCALL.txt")
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"{CONFIG_UI['nombre_proyecto']}\n")
        f.write(f"{CONFIG_UI['institucion']}\n")
        f.write("="*60 + "\n\n")

        for clave, valor in datos.items():
            f.write(f"{clave}: {valor}\n")
    print(f"\nReporte generado: {nombre_archivo}")

def generar_pdf(datos):
    nombre_pdf = os.path.join(CARPETA_RESULTADOS, "Reporte_SCALL.pdf")
    doc = SimpleDocTemplate(nombre_pdf, pagesize=letter)
    styles = getSampleStyleSheet()
    
    estilo_titulo = ParagraphStyle(
        name="Titulo",
        parent=styles["Title"],
        alignment=TA_CENTER
    )

    styles.add(ParagraphStyle(name="Center",
                           parent=styles["Heading2"],
                           alignment=TA_CENTER))

    elementos = []

    elementos.append(Spacer(1, 20))
    elementos.append(Paragraph(CONFIG_UI["nombre_proyecto"], estilo_titulo))
    elementos.append(Spacer(1, 10))
    elementos.append(Paragraph(CONFIG_UI["institucion"], styles["Center"]))
    elementos.append(Spacer(1, 20))

    styles.add(ParagraphStyle(name="Justificado",
                           parent=styles["Normal"],
                           alignment=TA_JUSTIFY))

    elementos.append(Paragraph('Para que el proyecto fuera más que una buena intención, era necesario cuantificar su potencial.' \
    ' El desafío era medir con precisión el área del techo del edificio, que no es un rectángulo simple, sino un polígono irregular' \
    ' con lados de diferentes longitudes. Por esta razón, una fórmula de "largo por ancho" era inútil. Así que se aplicó un método' \
    ' específico llamado la "fórmula del área de Gauss" (también conocida como "fórmula de la lazada"), una herramienta poderosa' \
    ' para calcular el área de cualquier polígono a partir de las coordenadas de sus vértices. Facilitando el como teniamos que crear un' \
    ' codigo automatico y de resultados a partir de eso valores', styles["Justificado"]))

    elementos.append(Paragraph("Resumen del Sistema de Captación de Agua Pluvial", styles["Heading2"]))
    elementos.append(Spacer(1, 12))

    for clave, valor in datos.items():
        texto = f"<b>{clave}:</b> {valor}"
        elementos.append(Paragraph(texto, styles["Normal"]))
        elementos.append(Spacer(1, 8))

    elementos.append(Spacer(1, 20))
    elementos.append(Paragraph(
        "Conclusión: El sistema SCALL permite aprovechar agua de lluvia mediante reciclaje PET, "
        "generando una solución sustentable y viable para la unidad académica.",
        styles["Italic"]
    ))

    doc.build(elementos)

    print(f"Reporte PDF generado: {nombre_pdf}")

def main():
    bienvenida()

    if not verificacion():
        return

    print("Ahora veremos el area y volumen de agua pluvial que se puede captar en la UNRC.")
    print(f"\nÁrea total UNRC: {MtSll.area:.2f} m²")
    print(f"Volumen máximo captable: {MtSll.volumen_captable:.2f} m³\n")

    porcentaje = seleccionar_porcentaje()
    area_c, vol_c = MtSll.calcular_volumen_captable(porcentaje)

    print(f"\nÁrea seleccionada: {area_c:.2f} m²")
    print(f"Volumen captable: {vol_c:.2f} m³\n")

    tipo, cant = seleccionar_botellas()
    litros, m3_almacen = MtSll.calcular_capacidad_almacenamiento(tipo, cant)

    print(f"\nCapacidad de almacenamiento: {litros:.0f} litros ({m3_almacen:.2f} m³)")

    util = vol_c
    if preguntar_si_no("¿Aplicar descarte inicial de 5 mm para limpieza? (Si/No): ") == "si":
        util = MtSll.calcular_descarte(area_c, vol_c)
        print(f"Volumen útil post-descarte: {util:.2f} m³")

    porcentaje_sistema = (m3_almacen / util * 100) if util > 0 else 0
    print(f"Capacidad del sistema respecto al volumen captable: {porcentaje_sistema:.2f}%\n")

    if preguntar_si_no("¿Está lloviendo en la UNRC? (Si/No): ") == "si":
        print("\nSistema activado:\n")
        print(MtSll.activado)
    else:
        print("\nEsperando lluvia para iniciar monitoreo...")
    
    datos_reporte = {
    "Área total UNRC (m²)": f"{MtSll.area:.2f}",
    "Área seleccionada (m²)": f"{area_c:.2f}",
    "Volumen captable (m³)": f"{vol_c:.2f}",
    "Capacidad de almacenamiento (m³)": f"{m3_almacen:.2f}",
    "Volumen útil final (m³)": f"{util:.2f}",
    "Porcentaje de aprovechamiento (%)": f"{porcentaje_sistema:.2f}"
    }
    generar_reporte(datos_reporte)
    generar_pdf(datos_reporte)

if __name__ == "__main__":
    main()