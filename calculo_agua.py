import numpy as np

# Datos iniciales Chalco
techo_area = 4297 # m2
lluvia_anual = 583 # mm

def calcular_volumen(area, lluvia):
    coeficiente = 0.9 # Cambio hecho desde mi PC
    return area * lluvia * coeficiente

print(f"Volumen total: {calcular_volumen(techo_area, lluvia_anual)} litros")
