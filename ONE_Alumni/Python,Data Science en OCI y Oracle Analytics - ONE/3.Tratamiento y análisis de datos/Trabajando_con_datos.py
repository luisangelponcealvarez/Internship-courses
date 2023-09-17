import pandas as pd

# Esto es para mostrar 15 elementos
pd.set_option("display.max_rows", 15)

# Aquí importamos los datos desde un archivo
dataset = pd.read_csv("./data/alquiler.csv", sep=";")

# Aquí mostramos los datos
print(dataset)

# Esto es para ver la descripción
print(dataset.describe())
