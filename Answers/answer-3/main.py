import pandas as pd
import csv
df = pd.read_csv('main.csv')
df.head()
df_sorted = df.sort_values(['Red Cards', 'Yellow Cards'], ascending=(False, False))
df_sorted[['Team', 'Yellow Cards', 'Red Cards']]
with open('answer1.csv', 'w') as f:
    writer = csv.writer(f)