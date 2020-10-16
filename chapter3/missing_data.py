import numpy as np
import pandas as pd


d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
# Creating a data frame using a dictionary
df = pd.DataFrame(d)
print(df)
# drops any rows with nan values
print(df.dropna())
# drops any columns with nan values
print(df.dropna(axis=1))
# keeps row if 2 or more non NaN values
print(df.dropna(thresh=2))
# fills any NaN value in data frame with the value given
print(df.fillna(value="Fill"))
# fills any NaN value in df['A'](column 'A') with the mean of the row
print(df['A'].fillna(value=df['A'].mean()))
