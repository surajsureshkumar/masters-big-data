import pandas as pd

df = pd.read_csv('extra.csv')

df = df.drop(
    ['IMDb_ID.type', 'MPAA_film_ratingLabel.type', 'MPAA_film_ratingLabel.xml:lang'
        , 'box_office.type', 'box_office_currencyLabel.type', 'box_office_currencyLabel.xml:lang',
     'cost.datatype', 'cost.type', 'distributorLabel.type', 'distributorLabel.xml:lang', 'titleLabel.type',
     '_id', 'box_office.datatype'], axis=1)
df['IMDb_ID.value'] = df['IMDb_ID.value'].str[2:]
df = df[df['box_office_currencyLabel.value'] == 'United States dollar']
df = df.dropna(subset=['IMDb_ID.value'])
df['IMDb_ID.value'] = df['IMDb_ID.value'].astype('Int64')
df['cost.value'] = df['cost.value'].astype('Int64')
df = df.drop_duplicates(subset=['IMDb_ID.value'])
df.rename(columns={'IMDb_ID.value': 'id'}, inplace=True)
df.to_csv('final_data1.csv', index=False)
