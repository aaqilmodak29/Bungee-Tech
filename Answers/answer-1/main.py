import pandas as pd
import csv

df = pd.read_csv('main.csv')
df.head()
df_grouped = df.groupby((df.Year//10)*10).sum()
del df_grouped['Year']
df_grouped.head()
with open('answer1.csv', 'w') as f:
    writer = csv.writer(f)