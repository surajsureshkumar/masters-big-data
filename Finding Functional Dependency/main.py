import numpy as np
import pandas as pd

tsv_file1 = "title.csv"
tsv_file2 = "movie_genre_mapping.csv"
tsv_file3 = 'title_actor.tsv'
tsv_file4 = 'member.csv'
tsv_file5 = 'title_actor_character.csv'
tsv_file6 = 'genre_movie_genre_id.csv'

"""
The code comment is a doc string cause my pycharm is issuing errors for line comments don't know the reason
The file is read into the dataframe
Backslash N values are replaced by NaN and dropped
From the data frame we are selecting runtimeMinutes which are greater than 90
We are applying a inner join on the dataframe and joining on tconst which is common in most of the tables
Suffix were added cause pycharm was issuing error for the join without suffix
All I did was join using inner join on a column and removed the extra columns created due to the suffix and 
created the csv file
Did not include the index for the data file
"""
df1 = pd.read_csv(tsv_file1, usecols=["tconst", "titleType", "startYear", "runtimeMinutes", "averageRating"])

df1.replace(r'\N', np.NaN, inplace=True)
df1.dropna(inplace=True)
df1 = df1[df1.runtimeMinutes.astype(int) >= 90]
df1 = df1.join(pd.read_csv(tsv_file2), on='tconst', how='inner', lsuffix='', rsuffix='_right') \
    .join(pd.read_table(tsv_file3, sep='\t'), on='tconst', how='inner', lsuffix='', rsuffix='_right2') \
    .join(pd.read_csv(tsv_file4, usecols=['nconst', 'birthYear']), on='nconst', how='inner', lsuffix='',
          rsuffix='_right3') \
    .join(pd.read_csv(tsv_file5), on='tconst', how='inner', lsuffix='',
          rsuffix='_right4')\

df1 = df1.join(pd.read_csv(tsv_file6), on='tconst', how='inner', lsuffix='',
               rsuffix='_right5')

df1.drop(['tconst_right', 'tconst_right2', 'nconst_right3', 'tconst_right4', 'nconst_right4', 'tconst_right5',
          'genres_right5'], axis=1).to_csv('new_relation.csv', index=False)
