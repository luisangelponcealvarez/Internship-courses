import pandas as pd
import matplotlib.pyplot as plt

plt.rc("figure", figsize=(14, 6))

datos = pd.read_csv("./alquiler_residencial.csv", sep=";")
print(datos.head(10))

# esto es un boxplot
print(datos.boxplot(["Valor"]))

datos[datos["Valor"] >= 500000]

valor = datos["Valor"]
Q1 = valor.quantile(0.25)
Q3 = valor.quantile(0.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ

seleccion = (valor >= limite_inferior) & (valor <= limite_superior)
datos_new = datos[seleccion]
print(datos_new.boxplot(["Valor"]))

