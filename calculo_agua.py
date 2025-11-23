import numpy as np

# Datos iniciales Chalco
medida_enfrente = 44.33 # m
medida_atras = 46.7 # m
medida_lado_izquierdo = 94.37 # m
medida_lado_derecho = 94.48 # m
area = (((medida_enfrente + medida_atras) / 2) * ((medida_lado_izquierdo + medida_lado_derecho) / 2)) # m2
lluvia_anual_chalco = 583.3 # mm
lluvia_anual = lluvia_anual_chalco / 1000 # Convertir mm a m3
coeficiente = 0.9
volumen = area * lluvia_anual * coeficiente



print("\nCálculo del area volumen para captación en la UNRC Chalco:")
print(f"\nArea total del techo de la UNRC Chalco: {area: .2f} m²")
print(f"Volumen total: {volumen: .2f} M³\n")

modulos_requeridos = volumen / .018  # Cada módulo almacena 180 litros = 0.18 m3
print("Para almacenar todo el volumen de agua pluvial recolectada en la UNRC Chalco, se requieren los siguientes módulos:\n")
print(f"Módulos de almacenamiento requeridos (180 L cada uno): {modulos_requeridos: .0f} módulos\n")

def porcentaje_area():
    while True: 
        porcentaje_piloto = float(input("1. Ingrese el Porcentaje de Área de Techo a Captar (ej. 5 para 5%): "))
        if 0 < porcentaje_piloto <= 100:
            area_captada = area * (porcentaje_piloto / 100)
            volumen_piloto = area_captada * lluvia_anual * coeficiente
            print(f"\nUtilizando un {porcentaje_piloto}% del area de la UNRC obtendriamos: {area_captada:.2f} m² = {volumen_piloto:.2f} m³ de agua captada\n")
            break
        else:
            print("Porcentaje debe estar entre 0 y 100.")
            continue # Vuelve a iniciar el ciclo actual
                
porcentaje_area() # Función activada e inicio de esta   