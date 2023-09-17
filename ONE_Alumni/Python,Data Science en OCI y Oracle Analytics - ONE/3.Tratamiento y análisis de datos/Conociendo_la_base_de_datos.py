import pandas as pd

datos = pd.read_csv("./data/alquiler.csv", sep=";")

# Estos son los tipos de datos
dtypes = datos.dtypes
print(dtypes)

tipo_de_datos = pd.DataFrame(datos.dtypes, columns=["Tipos de datos"])
tipo_de_datos.columns.name = "Variables"

print("Esto es la forma más organizada: ")
print(tipo_de_datos)

datos.shape[0]
datos.shape[1]

print(
    "La base de datos presenta {} registros (inmuebles) y {} variables".format(
        datos.shape[0], datos.shape[1]
    )
)
