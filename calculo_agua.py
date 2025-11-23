import numpy as np

# Datos iniciales Chalco
medida_enfrente = 44.33 # m
medida_atras = 46.7 # m
medida_lado_izquierdo = 94.37 # m
medida_lado_derecho = 94.48 # m
area_formula_triangulo1 = (medida_enfrente + medida_atras) / 2
area_formula_triangulo2 = (medida_lado_izquierdo + medida_lado_derecho) / 2
techo_area_chalco = (area_formula_triangulo1 * area_formula_triangulo2) # m2
lluvia_anual_chalco = 583.3 # mm
techo_area = techo_area_chalco
lluvia_anual = lluvia_anual_chalco / 1000 # Convertir mm a m

def calcular_volumen(area, lluvia):
    coeficiente = 0.9 # Cambio hecho desde mi PC
    return area * lluvia * coeficiente
print("Cálculo de volumen de agua de lluvia recolectada en Chalco")
print(f"Volumen total: {calcular_volumen(techo_area, lluvia_anual)} Metros Cúbicos")
