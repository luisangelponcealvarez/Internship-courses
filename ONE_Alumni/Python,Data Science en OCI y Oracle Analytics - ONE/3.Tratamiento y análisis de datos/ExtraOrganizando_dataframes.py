import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

df = pd.DataFrame(data, list("321"), list("zyx"))
print(df)

df.sort_index(inplace=True)
print(df)

df.sort_index(inplace=True, axis=1)
print(df)

df.sort_values(
    by="x",
    inplace=True,
)
print(df)

df.sort_values(
    by="3",
    axis=1,
    inplace=True,
)
print(df)
