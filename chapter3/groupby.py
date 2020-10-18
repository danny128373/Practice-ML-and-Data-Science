import pandas as pd

# Dictionary that's going to be used for dataframe
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

# Creating data frame
df = pd.DataFrame(data)
print(df)
# groupby company (only returns object location ref)
byComp = df.groupby('Company')
# when you use the aggregate function you can see your df using groupby
# only takes number columns to consideration when taking the mean
print(byComp.mean())
# only takes number columns to consideration when finding sum by company
print(byComp.sum())

print(df.groupby('Company').describe())
