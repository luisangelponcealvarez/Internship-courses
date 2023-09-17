import pandas as pd

# Series
data = [1, 2, 3, 4, 5]

s = pd.Series(data)
print(s)

index = ["Linea" + str(i) for i in range(5)]
print(index)

s = pd.Series(data=data, index=index)
print(s)

data = {"Linea" + str(i): i + 1 for i in range(5)}
print(data)

s1 = s + 2
print(s1)

s2 = s1 + s
print(s2)
