import numpy as np
import pandas as pd

df = pd.read_csv('new_relation.csv')

vals = df[['nconst', 'id']].value_counts()  # counting values nconst unique values

nconst = [i[0] for i in vals[vals.values > 1].index]  # seaprating value of nconst which are greater than 1
# taking ids which are greater than 1( which is repeated more than once nconst and id together)
ids = [i[1] for i in vals[vals.values > 1].index]


def new_col(row):
    """
    Passing each and every row of dataframe
    :param row:
    :return:
    """
    if row['nconst'] in nconst:  # checking if row nconst in nconst list
        idx = nconst.index(row['nconst'])  # if present checking the index of the nconst
        # if that index value is in row id then returning 0 determining duplicate or else return 1
        if ids[idx] == row['id']:
            return 0
    return 1


df['col'] = df.apply(new_col, axis=1)  # got 0 and 1s in new columns

remove_movies = df[
    df.col == 0].tconst.values  # taking columns which have 0 value and the tconst value and storing in remove_movies

df['col'] = df.tconst.apply(
    lambda x: 0 if x in remove_movies else 1)  # if row value in remove_movies column is assigned 0 or else 1
df = df[df.col == 1]  # then columns which have 1
df.replace(r'\N', np.NaN, inplace=True)
df.drop(['col'], axis=1).to_csv('find_dependencies.tsv', index=False)
