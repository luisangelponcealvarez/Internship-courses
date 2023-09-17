import pandas as pd

dataset = pd.read_csv("db.csv", sep=";", index_col=0)

dataset.head()

dataset["Valor"]

type(dataset["Valor"])

# seleccionando lineas [¡:j]
valor3 = dataset[0:3]

# .loc para selecciones
dataset.loc["Año"]

# .iloc por la posición
dataset.iloc[[1]]
dataset.iloc[1:4]
