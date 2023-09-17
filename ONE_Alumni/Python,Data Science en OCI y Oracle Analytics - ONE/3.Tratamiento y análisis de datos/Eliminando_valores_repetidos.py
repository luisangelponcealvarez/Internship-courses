import pandas as pd

datos = pd.read_csv("./data/alquiler.csv", sep=";")
headDatos = datos.head(10)
print(headDatos)

# Lista de la columna de Tipo
Tipo = datos["Tipo"]
print(Tipo)

# Eliminar los duplicados
Tipo.drop_duplicates(inplace=True)
print(Tipo)
