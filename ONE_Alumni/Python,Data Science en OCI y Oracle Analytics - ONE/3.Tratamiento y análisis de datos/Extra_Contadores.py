import pandas as pd 
s = pd.Series(list('asdfsdfsfsdfsdfwwe'))
print(s)

print(s.unique())

print(s.value_counts())

datos = pd.read_csv('alquiler.csv', sep=';')
print(datos.head(10))

print(datos.Tipo.unique())

print(datos.Tipo.value_counts())

