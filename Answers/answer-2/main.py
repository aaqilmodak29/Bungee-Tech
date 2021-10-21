import pandas as pd
df = pd.read_csv('main.csv')
df.head()
df_grouped = df.groupby('occupation').agg({'age': ['min', 'max']})
df_grouped.to_csv('Grouped-Data.csv')
