import pandas as pd

df = pd.read_csv('main.csv')
df.head()
df_grouped = df.groupby((df.Year//10)*10).sum()
del df_grouped['Year']
df_grouped.head()
df_grouped.to_csv('Grouped-Data.csv')
