import pandas as pd

# reading the files into the dataframe and for df1 using columns which are necessary
df = pd.read_table('title.basics.tsv.gz', sep='\t')
df1 = pd.read_table('title.principals.tsv.gz', sep='\t', usecols=['tconst', 'nconst', 'characters'])
df2 = pd.read_table('title.crew.tsv.gz', sep='\t')
df3 = pd.read_csv('title_producer.csv')

# removing the tt from tconst and the nm from nconst
df['tconst'] = df['tconst'].str[2:]
df1['tconst'] = df1['tconst'].str[2:]
df2['tconst'] = df2['tconst'].str[2:]
df1['nconst'] = df1['nconst'].str[2:]

# merging df with df2 to get the directors and writers and df and df1 to get the actor id  and roles and df and df3 to
# get the producers
df = df.merge(df2, on='tconst', how='inner')
df = df.merge(df1, on='tconst', how='inner')
df = df.merge(df3, on='tconst', how='inner')

# replacing the \N with ' '
df.replace(r'\N', ' ', inplace=True)

# splitting genres by ,(comma) to the array of values
df['genres'] = df['genres'].apply(lambda x: str(x).split(','))
# replacing all the nm in directors and writers
df['directors'] = df['directors'].str.replace('nm', '')
df['writers'] = df['writers'].str.replace('nm', '')
# splitting directors, writers and producers to get values in arrays and the whole as a array
df['directors'] = df['directors'].apply(lambda x: str(x).split(','))
df['writers'] = df['writers'].apply(lambda x: str(x).split(','))
df['producers'] = df['producers'].apply(lambda x: str(x).split(','))

# renaming the columns
df.rename(columns={'nconst': 'actor.id', 'characters': 'actor.roles', 'tconst': 'id'}, inplace=True)
# creating the csv file and dropping the index by setting it to false
df.to_csv('Final_data.csv', index=False)
