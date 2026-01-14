import matplotlib.pyplot as plt

# Hypothetical coordinates for UAC map with PET and HDPE containers
points = {
    "Entrada Principal": (2, 8),
    "Edificio A": (5, 9),
    "Edificio B": (8, 6),
    "Edificio C": (3, 4),
    "Cafetería": (7, 3),
    "Centro de la UNRC": (5, 5),
    "Contenedor PET 1": (4, 7),
    "Contenedor PET 2": (7, 5),
    "Contenedor HDPE 1": (4, 3),
    "Contenedor HDPE 2": (6, 2),
}

x = [coord[0] for coord in points.values()]
y = [coord[1] for coord in points.values()]

plt.figure(figsize=(8, 8))
plt.scatter(x, y)

for label, (px, py) in points.items():
    plt.text(px + 0.1, py + 0.1, label, fontsize=9)

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Plano Cartesiano – Distribución Estratégica de Contenedores PET y HDPE")
plt.grid(True)

plt.show()
