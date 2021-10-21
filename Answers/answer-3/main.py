import pandas as pd
df = pd.read_csv('main.csv')
df.head()
df_sorted = df.sort_values(['Red Cards', 'Yellow Cards'], ascending=(False, False))
df_sorted[['Team', 'Yellow Cards', 'Red Cards']]
df_sorted.to_csv('Grouped-Data.csv')
