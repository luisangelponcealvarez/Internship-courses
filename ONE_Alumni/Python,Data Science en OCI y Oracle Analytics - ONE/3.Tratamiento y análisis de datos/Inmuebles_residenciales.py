import pandas as pd

datos = pd.read_csv("./data/alquiler.csv", sep=";")
datos.head(10)

print(list(datos["Tipo"].drop_duplicates()))

residencial = [
    "Habitación",
    "Casa",
    "Departamento",
    "Casa en condominio",
    "Casa comercial",
    "Casa de villa",
]

print(residencial)

seleccion = datos["Tipo"].isin(residencial)
print(seleccion)

datos_residencial = datos[seleccion]
print(datos_residencial)

print(list(datos_residencial["Tipo"].drop_duplicates()))

datos_residencial.index = range(datos_residencial.shape[0])
print(datos_residencial)
