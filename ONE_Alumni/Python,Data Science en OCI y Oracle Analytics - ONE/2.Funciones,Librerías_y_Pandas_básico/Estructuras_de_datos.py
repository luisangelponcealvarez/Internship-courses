import pandas as pd

# Creando una series a partir de una lista
carros = ["jatta variant", "passat", "crossfox"]
pd.Series(carros)

# DataFrame
carros = [
    {"Nombre": "jetta variant", "Año": 2002},
    {"Nombre": "passat", "Año": 5226},
    {"Nombre": "crossfox", "Año": 4155},
]
dataset = pd.DataFrame(carros)
print(dataset)

# Data Frame dicciónarios
datos = {
    "Nombre": ["jetta variant", "passat", "crossfox"],
    "Motor": ["Motor 4.0 turbo", "Motor Diesel"],
    "Año": [65132, 6565, 5565],
    "Valor": [5565, 6566, 5133],
}

dataset = pd.DataFrame(datos)
print(dataset)

# Data Frame archivo externo
dataset = pd.read_csv("db.csv", sep=";", index_col=0)
print(dataset)
