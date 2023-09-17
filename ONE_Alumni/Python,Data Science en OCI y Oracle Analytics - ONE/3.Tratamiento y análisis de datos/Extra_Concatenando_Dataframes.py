import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data)

df1 = pd.DataFrame(data=data)
print(df1)

# Aquí le ponemos nombre a las filas
index = ["Linea" + str(i) for i in range(3)]
print(index)

df1 = pd.DataFrame(data=data, index=index)
print(df1)

# Aquí le ponemos nombre a las columns
columns = ["columns" + str(i) for i in range(3)]
print(columns)

df1 = pd.DataFrame(data=data, index=index, columns=columns)
print(df1)

# Aquí esta pero en dicciónario
data = {
    "columna0": {"Linea0": 1, "Linea1": 4, "Linea2": 7},
    "Columna1": {"Linea0": 2, "Linea1": 5, "Linea2": 8},
    "Columna2": {"Linea0": 3, "Linea1": 6, "Linea2": 9},
}
print(data)

df2 = pd.DataFrame(data)
print(df2)

# Aquí esta pero en tuplas
data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(data)

df3 = pd.DataFrame(data, index=index, columns=columns)
print(df3)

# Esto cambia los datos a A si todos cumplen con la condición
df1[df1 > 0] = "A"
print(df1)

df2[df2 > 0] = "B"
print(df2)

df3[df3 > 0] = "C"
print(df3)

# juntando todo en vertical
df4 = pd.concat([df1, df2, df3])
print(df4)

# juntando todo en horizontal
df4 = pd.concat([df1, df2, df3], axis=1)
print(df4)
