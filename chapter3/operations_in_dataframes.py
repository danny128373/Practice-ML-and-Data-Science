
import pandas as pd
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [
                  444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})

# Gets unique values from col2
print(df['col2'].unique())
# Gets how many unique values from col2 (you could use len as well)
print(df['col2'].nunique())
# Returns how many times the value appears
print(df['col2'].value_counts())
# Returns all the rows where col1 happened to be greater than 2
print(df[df['col1'] > 2])


def times2(x):
    return x*2


# You can pass any custom function and send your data frame or a subset of your data frame as an argument
print(df['col1'].apply(times2))
# Most useful when using lambda expressions
print(df['col2'].apply(lambda x: x*2))
# To delete a column, axis=0 to delete a row
print(df.drop('col1', axis=1))
# Returns list of column names (columns is an attribute)
print(df.columns)
# Returns details of the index
print(df.index)
# sort works about the same as sql
df.sort_values('col2')

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)

df.pivot_table(values='D', index=['A', 'B'], columns=['C'])
