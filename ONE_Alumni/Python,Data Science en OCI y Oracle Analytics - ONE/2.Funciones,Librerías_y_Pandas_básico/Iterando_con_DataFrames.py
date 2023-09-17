import pandas as pd

dataset = pd.read_csv("db.csv", encoding="utf-8", errors="ignore")

print(dataset.head())

list(dataset.iterrows())

for index, row in dataset.iterrows():
    if 2020 - row.Año != 0:
        dataset.loc[index, "km_media"] = row.kilometraje / (2020 - row.Año)
    else:
        dataset.loc[index, "km_media"] = 0

print(dataset)
