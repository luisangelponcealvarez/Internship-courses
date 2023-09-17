import pandas as pd

"l1 l2 l3 l4".split()

data = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16)]
df = pd.DataFrame(data, "l1 l2 l3 l4".split(), "c1 c2 c3 c4".split())
print(df)

c1 = df["c1"]
print(c1)

select = df[["c1", "c3"]]
print(select)

selecciónIndise = df[1:3]
print(selecciónIndise)

selecciónColumnas = df[1:][["c3", "c1"]]
print(selecciónColumnas)

dataColum = df.loc["l3"]
print(dataColum)

dataColum2 = df.loc[["l3", "l2"]]
print(dataColum2)

loc = df.loc["l1", "c2"]
print(loc)
iloc = df.iloc[0, 1]
print(iloc)

locSelect = df.loc[["l3", "l1"], ["c4", "c1"]]
print(locSelect)

ilocSelect = df.loc[[2, 0], [3, 0]]
print(ilocSelect)
