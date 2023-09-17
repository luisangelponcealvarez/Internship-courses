import pandas as pd

datos = pd.read_csv('./alquiler_residencial.csv', sep=';')
print(datos.head(10))

# esto es para buscar los valores no isnull
isnull = datos.isnull()
print(isnull)

# esto es para buscar los valores no nulos
notnull = datos.notnull()
print(notnull)

# las informaciones de la base de datos
info = datos.info()
print(info)

# esto es para ver true o false si es un valor nulo en la columna Valor
columna = datos[datos['Valor'].isnull()]
print(columna)

A = datos.shape[0]
datos.dropna(subset = ['Valor'], inplace=True)
B = datos.shape[0]
print(A - B)

