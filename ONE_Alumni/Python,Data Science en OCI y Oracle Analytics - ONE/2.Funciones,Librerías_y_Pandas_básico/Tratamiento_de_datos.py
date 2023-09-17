import pandas as pd

dataset = pd.read_csv("db.csv", sep=";", index_col=0)

dataset.info()

dataset.Kilometraje.isna()

dataset[dataset.Kilometraje.isna()]

dataset.fillna(0, inplace=True)

dataset.query("Cero_km == True")

dataset = pd.read_csv("db.csv", sep=";")

dataset.dropna(subset=["kilometraje"], inplace=True)
print(dataset)
