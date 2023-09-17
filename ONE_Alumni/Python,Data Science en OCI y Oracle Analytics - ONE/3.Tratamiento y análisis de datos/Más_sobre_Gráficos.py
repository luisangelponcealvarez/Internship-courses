import pandas as pd
import matplotlib.pyplot as plt

plt.rc("figure", figsize=(15, 10))
datos = pd.read_csv("./alquiler_residencial_sin_outliers.csv", sep=";")
print(datos.head())

area = plt.figure()


g1 = area.add_subplot(2, 2, 1)
g2 = area.add_subplot(2, 2, 2)
g3 = area.add_subplot(2, 2, 3)
g4 = area.add_subplot(2, 2, 4)

# crear graficos
g1.scatter(datos.Valor, datos.Area)
g1.set_title("Valor x Area")

g2.hist(datos.Valor)
g2.set_title("Histograma")

datos_g3 = datos.Valor.sample(100)
datos_g3.index = range(datos_g3.shape[0])
g3.plot(datos_g3)
g3.set_title('Muestra (Valor)')

grupo = datos.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values
g4.bar(label,valores)
g4.set_title('Valor Medio por Tipo')

print(area)

area.savefig('Grafico.png',dpi = 300, bbox_inches = 'tight')