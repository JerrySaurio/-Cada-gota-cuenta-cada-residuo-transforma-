import pandas as pd
import matplotlib.pyplot as plt

datos = "datos_lluvia_chalco.csv"

df = pd.read_csv(datos, nrows=64)
print("\nDatos de lluvia mensual en Chalco (mm):\n")
print(df.head(5))


meses = df[["AÑO", "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]]
print("\nMeses del año:\n")
print(meses)
df = pd.read_csv("datos_lluvia_chalco.csv", nrows=64)[["AÑO", "ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]]

ax = meses.plot.bar(x ="AÑO", y=["ENERO"], rot=0)
plt.xticks(rotation=90)
plt.show()