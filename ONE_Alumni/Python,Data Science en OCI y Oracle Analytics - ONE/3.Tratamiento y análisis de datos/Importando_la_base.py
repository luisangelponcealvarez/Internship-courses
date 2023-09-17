import pandas as pd

datos = pd.read_csv("./data/alquiler.csv", sep=";")


print(datos)

# Esto es para la info de los datos
print("Esta es la info de los datos")
datos.info()

# Esto es para la cabesera de los datos
print("Estos son los primeros datos")
print(datos.head(10))
