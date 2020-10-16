import numpy as np
import pandas as pd
from numpy.random import randn

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}
print(pd.Series(data=my_data, index=labels))

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
print(ser1)

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print(df['W'][3])
print(df[['W', 'Z']])

df['new'] = df['W'] + df['Y']
print(df)

df.drop('new', axis=1, inplace=True)
print(df)

df.drop('E', inplace=True)
print(df)

# label selecting
print(df.loc['A'])
# index row selecting
print(df.iloc[2])

de = df[(df['Z'] > 0) | (df['Y'] > 1)]
print(de)

# reset index to default (needs argument of inplace=True in order to take effect immediately)
# Creates a new column for the old index
df.reset_index()

newind = 'CA NY WY OR'.split()
df['States'] = newind
print(df)

# Sets the index(labels), (needs argument of inplace=True in order to take effect immediately)
# Replaces index column and you lose your old column
df.set_index('States')
