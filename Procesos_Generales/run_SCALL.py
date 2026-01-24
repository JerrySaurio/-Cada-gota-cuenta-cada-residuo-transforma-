from Config_rutas import CARPETA_GRAFICAS, CARPETA_RESULTADOS

print("----------------------------------------------")
print("    Generación de Gráficas e Infome Final")
print("----------------------------------------------")

def generador_grafica_informe():
    try:
        print("Generando gráfica de medidas de unidad académica...")
        import Grafica_Medidas_unidad_academica
        Grafica_Medidas_unidad_academica.Grafica_Medidas()
        print("Gráfica de medidas completada.\n")
    except Exception as e:
        print(f"Error en gráfica de medidas: {e}\n")

    try:
        print("Generando gráfica de lluvia máxima al dia...")
        import Grafica_min_max_media_24h
        Grafica_min_max_media_24h.Grafica_24h()
        print("Gráfica de máxima la dia completada.\n")
    except Exception as e:
        print(f"Error en gráfica de lluvia máxima al dia: {e}\n")

    try:
        print("Generando gráfica de lluvia máxima al mes...")
        import Grafica_min_max_media_mensual
        Grafica_min_max_media_mensual.Grafica_Mensual()
        print("Gráfica de máxima al mes completada.\n")
    except Exception as e:
        print(f"Error en gráfica de lluvia máxima al mes: {e}\n")

    try:
        print("Generando gráfica lluvia histórica...")
        import Grafica_mm_anual_historica
        Grafica_mm_anual_historica.Datos_Mensuales()
        print("Gráfica de lluvia historica completada.\n")
    except Exception as e:
        print(f"Error en gráfica de lluvia histórica: {e}\n")

    try:
        print("Generando gráfica de puntos de recolección PET...")
        import Grrafica_puntos_PET
        Grrafica_puntos_PET.Grafica_puntos_pet()
        print("Gráfica de puntos de recolección PET completada.\n")
    except Exception as e:
        print(f"Error en gráfica de puntos de recolección PET: {e}\n")

    try:
        print("Generando informe PDF final...")
        import Generar_Informe
        Generar_Informe.generar_informe()
        print("📄 Informe PDF generado correctamente.\n")
    except Exception as e:
        print(f"Error en el informe PDF final: {e}")

generador_grafica_informe()

print(f"Imagenes guardadas en: {CARPETA_GRAFICAS}")
print(f"Reportes e informe guardados en: {CARPETA_RESULTADOS}\n")

print("----------------------------------------------")
print("                Finalizado")
print("----------------------------------------------")
