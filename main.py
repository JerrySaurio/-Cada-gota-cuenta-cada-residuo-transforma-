import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QTableWidget, QTableWidgetItem, QComboBox, QPushButton,
    QHBoxLayout, QLabel, QLineEdit
)

class Dashboard(QMainWindow):
    def __init__(self, datos_lluvia_chalco_csv):
        super().__init__()
        self.setWindowTitle("Dashboard Interactivo con CSV y Filtros")
        self.setGeometry(100, 100, 1100, 600)

        # Leer CSV
        self.df = pd.read_csv("datos_lluvia_chalco.csv", nrows=64)[["AÑO", "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]]

        # Tabla
        self.table = QTableWidget()
        self.table.setRowCount(len(self.df))
        self.table.setColumnCount(len(self.df.columns))
        self.table.setHorizontalHeaderLabels(self.df.columns)
        for i in range(len(self.df)):
            for j, col in enumerate(self.df.columns):
                self.table.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

        # Combobox columnas
        self.x_combo = QComboBox(); self.x_combo.addItems(self.df.columns)
        self.y_combo = QComboBox(); self.y_combo.addItems(self.df.columns)

        # Tipo de gráfico
        self.chart_type_combo = QComboBox()
        self.chart_type_combo.addItems(["Línea", "Barras", "Dispersión"])

        # Filtros por rango (en columna X)
        self.min_input = QLineEdit(); self.min_input.setPlaceholderText("Mínimo")
        self.max_input = QLineEdit(); self.max_input.setPlaceholderText("Máximo")

        # Botón graficar
        self.btn_plot = QPushButton("Graficar")
        self.btn_plot.clicked.connect(self.update_plot)

        # Layout controles
        controls_layout = QHBoxLayout()
        controls_layout.addWidget(QLabel("X:")); controls_layout.addWidget(self.x_combo)
        controls_layout.addWidget(QLabel("Y:")); controls_layout.addWidget(self.y_combo)
        controls_layout.addWidget(QLabel("Tipo:")); controls_layout.addWidget(self.chart_type_combo)
        controls_layout.addWidget(QLabel("Filtro X:"))
        controls_layout.addWidget(self.min_input); controls_layout.addWidget(self.max_input)
        controls_layout.addWidget(self.btn_plot)

        # Gráfico inicial
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)

        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.table)
        layout.addLayout(controls_layout)
        layout.addWidget(self.canvas)
        self.setCentralWidget(central_widget)

    def update_plot(self):
        x_col = self.x_combo.currentText()
        y_col = self.y_combo.currentText()
        chart_type = self.chart_type_combo.currentText()

        # Filtrar datos
        df_filtered = self.df.copy()
        try:
            min_val = float(self.min_input.text()) if self.min_input.text() else None
            max_val = float(self.max_input.text()) if self.max_input.text() else None
            if min_val is not None:
                df_filtered = df_filtered[df_filtered[x_col] >= min_val]
            if max_val is not None:
                df_filtered = df_filtered[df_filtered[x_col] <= max_val]
        except:
            pass  # si no son números, ignora

        # Graficar
        self.ax.clear()
        if chart_type == "Línea":
            self.ax.plot(df_filtered[x_col], df_filtered[y_col], marker="o")
        elif chart_type == "Barras":
            self.ax.bar(df_filtered[x_col], df_filtered[y_col])
        elif chart_type == "Dispersión":
            self.ax.scatter(df_filtered[x_col], df_filtered[y_col])

        self.ax.set_xlabel(x_col)
        self.ax.set_ylabel(y_col)
        self.ax.set_title(f"{chart_type}: {y_col} vs {x_col}")
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard("datos_lluvia_chalco.csv")  # <-- pon aquí tu CSV
    window.show()
    sys.exit(app.exec_())