import pandas as pd

datos = pd.read_csv("./data/alquiler.csv", sep=";")
tamaño = datos.head(10)
print(tamaño)

clases = [0, 2, 4, 6, 100]
cuartos = pd.cut(datos.Cuartos, clases)
print(cuartos)

pd.value_counts(cuartos)

label = ["1 y 2 cuartos", "3 y 4 cuartos", "5 y 6 cuartos", "7 cuartos o mas"]
cuartos = pd.cut(datos.Cuartos, clases, labels=label)
print(pd.value_counts(cuartos))

cuartos = pd.cut(datos.Cuartos, clases, labels=label, include_lowest=True)
print(pd.value_counts(cuartos))
