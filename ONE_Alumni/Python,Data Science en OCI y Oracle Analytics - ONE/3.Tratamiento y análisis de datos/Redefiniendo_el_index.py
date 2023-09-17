import pandas as pd

datos = pd.read_csv("./data/alquiler.csv", sep=";")
headDatos = datos.head(10)
print(headDatos)

# Lista de la columna de Tipo
tipo_de_inmueble = datos["Tipo"]

# Eliminar los duplicados
tipo_de_inmueble.drop_duplicates(inplace=True)
print(tipo_de_inmueble)

# Este es el index
print("Este es el index: ")
indice = tipo_de_inmueble.index
print(indice)

# Esto es para el transformar a DataFrame y saber el tamaño de las filas
tipo_de_inmueble = pd.DataFrame(tipo_de_inmueble)
tamaño = tipo_de_inmueble.shape[0]
print("Este es el tamaño de los datos: ", tamaño)

# Generando valores
Generando = range(tipo_de_inmueble.shape[0])
print(Generando)

for i in range(tipo_de_inmueble.shape[0]):
    print(i)

tipo_de_inmueble = range(tipo_de_inmueble.shape[0])
print(tipo_de_inmueble.index)
print(tipo_de_inmueble)
tipo_de_inmueble.columns.name = "Id"
