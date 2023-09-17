import pandas as pd 
data = [0.5, None,None,0.52,0.54,None,None,0.59,0.6,None,0.7 ]

s = pd.Series(data)
print(s)

s.fillna(0)
print(s)

s.fillna(method='ffill')
print(s)

s.fillna(method='bfill')
print(s)

