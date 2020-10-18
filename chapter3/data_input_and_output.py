import pandas as pd

# File example is assigned to df
df = pd.read_csv(
    '/home/dm3f90/workspace/python/data_science_ml/chapter3/example')
# df is converted to csv, first argument is location
df.to_csv('chapter3/My_output.csv', index=False)

# File example is assigned to df
df = pd.read_excel(
    '/home/dm3f90/workspace/python/data_science_ml/chapter3/Excel_Sample.xlsx', sheet_name='Sheet1')
# df is converted to excel, first argument is location, second argument is sheet name
df.to_excel('chapter3/Excel_Sample2.xlsx', sheet_name='NewSheet')
# Essentially scrapes html for tables and each table is an element, df currently is a list of tables
# in this example there's only one table in this list
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

print(df)
