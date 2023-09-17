import pandas as pd

datos = pd.read_csv("./alquiler_residencial.csv", sep=";")
datosHead = datos.head(10)
print(datosHead)

# Selecciones solamente los inmuebles clasificados con tipo 'Departamento'
seleccion = datos["Tipo"] == "Departamento"
n1 = datos[seleccion].shape[0]
print(n1)

# Seleccione los inmuebles clasificados con tipos 'Casa', 'Casa en condominio' y 'Casa de villa'
seleccion = (
    (datos["Tipo"] == "Casa")
    | (datos["Tipo"] == "Casa en condominio")
    | (datos["Tipo"] == "Casa de villa")
)
n2 = datos[seleccion].shape[0]
print(n2)

# Seleccione los inmuebles con área entre 60 y 100 metros cuadrados, incluyendo los limites
seleccion = (datos["Area"] >= 60) & (datos["Area"] <= 100)
n3 = datos[seleccion].shape[0]
print(n3)

# Seleccione los inmuebles que tengan por lo menos 4 cuartos y alquiler menor que $2.000.00
seleccion = (datos["Cuarto"] >= 4) & (datos["Valor"] <= 2000)
n4 = datos[seleccion].shape[0]
print(n4)
