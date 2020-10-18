from sqlalchemy import create_engine
import pandas as pd

# creates a temporary sql engine in memory
engine = create_engine('sqlite:///:memory:')

# Essentially scrapes html for tables and each table is an element, df currently is a list of tables
# in this example there's only one table in this list
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# This engine is a connection
df[0].to_sql('my_table', engine)

sqldf = pd.read_sql('my_table', con=engine)
print(sqldf)
