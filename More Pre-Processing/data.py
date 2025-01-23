import pandas as pd
import numpy as np


def title():
    """
    Pre-processing
    :return:
    """
    # store files to a variable
    tsv_file1 = "title.basics.tsv.gz"
    tsv_file2 = "title.ratings.tsv.gz"

    # reading files using the read table
    df1 = pd.read_table(tsv_file1,
                        usecols=["tconst", "titleType", "primaryTitle", "originalTitle", "startYear", "endYear",
                                 "runtimeMinutes"])
    df2 = pd.read_table(tsv_file2, usecols=["tconst", "averageRating", "numVotes"])

    df1['tconst'] = df1['tconst'].str[2:]
    df2['tconst'] = df2['tconst'].str[2:]

    df1.replace(r'\N', np.NaN, inplace=True)
    df2.replace(r'\N', np.NaN, inplace=True)

    df2 = pd.merge(df1, df2, on='tconst', how="inner")
    df2.to_csv('title.csv', index=False)


def genre():
    """
        Pre-processing the title.basics.tsv.gz
        :return: None
        """
    tsv_file = "title.basics.tsv.gz"

    df = pd.read_table(tsv_file, usecols=[
        'genres'])  # using pd.read_table to read delimited file into dataframe and reading only the columns of genres
    df.replace(r'\N', np.NaN, inplace=True)  # replacing the \N with NaN

    dictionary = {}  # Initializing a dictionary

    # Function to keep the count of number of occurrences of each genre
    def count(x):
        global dictionary
        if type(x) == float:
            return
        for i in str(x).split(','):
            try:
                dictionary[i] += 1
            except:
                dictionary[i] = 1

    df.genres.apply(count)
    df_id = list(dictionary.keys())  # creating a list of dictionaries

    results = pd.DataFrame(data=df_id, columns=['genres'])
    results['genre_id'] = results.index

    results.to_csv('genres.csv', index=False)


def member():
    """

    :return:
    """
    tsv_file = "name.basics.tsv.gz"
    df = pd.read_table(tsv_file)

    df['nconst'] = df['nconst'].str[2:]

    df.replace(r'\N', np.NaN, inplace=True)
    df.drop(['primaryProfession', 'knownForTitles'], axis=1).to_csv('member.csv', index=False)


def characters():
    """

    :return:
    """
    tsv_file = "title.principals.tsv.gz"
    df = pd.read_table(tsv_file, usecols=['nconst', 'characters'])

    df.replace(r'\N', np.nan, inplace=True)
    df = df[df.characters.notnull()]

    df['nconst'] = df['nconst'].str[2:]
    df['characters'] = df['characters'].apply(lambda x: x[1:-1])

    df = df.explode("characters", ignore_index=True)

    df_clean = pd.DataFrame()
    df_clean['characters'] = df['characters'].unique()
    df_clean['characters'] = df_clean['characters'].apply(lambda x: x[1:-1])

    df_clean['id'] = df_clean.index

    df_clean.to_csv('characters.tsv', sep='\t', index=False)


def title_actor():
    """

    :return:
    """
    tsv_file1 = "title.principals.tsv.gz"

    df1 = pd.read_table(tsv_file1, usecols=['tconst', 'nconst', 'category'])

    df1 = df1[df1['category'].isin(['self', 'actor', 'actress'])]
    df1 = df1[['tconst', 'nconst']]

    df1['nconst'] = df1['nconst'].str[2:]
    df1['tconst'] = df1['tconst'].str[2:]

    df1.to_csv('title_actor.tsv', sep='\t', index=False)


def title_writers():
    """

    :return:
    """
    tsv_file = "title.crew.tsv.gz"

    df = pd.read_table(tsv_file, usecols=['tconst', 'writers'])

    df['tconst'] = df['tconst'].str[2:]
    df['writers'] = df['writers'].apply(lambda x: x.split('nm')[-1])

    df.replace(r'\N', np.NaN, inplace=True)
    df = df[df.writers.notnull()]

    df['writers'] = df.writers.apply(lambda x: str(x).split(','))
    df.explode("writers", ignore_index=True).to_csv('title_writers.csv', index=False)


def title_director():
    """

    :return:
    """
    tsv_file = "title.crew.tsv.gz"
    df = pd.read_table(tsv_file, usecols=["tconst", "directors"])

    df['tconst'] = df['tconst'].str[2:]

    df['directors'] = df.directors.apply(lambda x: str(x).split(','))
    df = df.explode("directors", ignore_index=True)
    df['directors'] = df['directors'].str[2:]

    df.replace(r'\N', np.NaN, inplace=True)
    df.directors.notnull()

    df.to_csv('title_directors.csv', index=False)


def title_producer():
    """

    :return:
    """
    tsv_file = "title.principals.tsv.gz"

    df = pd.read_table(tsv_file, usecols=['tconst', 'category', 'nconst'])

    df['tconst'] = df['tconst'].str[2:]
    df.replace(r'\N', np.NaN, inplace=True)
    df = df[df.category == 'producer']
    df['nconst'] = df['nconst'].str[2:]

    df = df[['tconst', 'nconst']]

    df.to_csv('title_producer.csv', index=False)


def title_actor_character():
    """

    :return:
    """

    tsv_file = "title.principals.tsv.gz"
    tsv_file2 = "characters.tsv"

    df1 = pd.read_table(tsv_file, usecols=['tconst', 'nconst', 'characters'], nrows=5000000)
    df2 = pd.read_table(tsv_file2, nrows=5000000)

    df1['characters'] = df1['characters'].apply(lambda x: x[2:-2])
    df1['characters'] = df1.characters.apply(lambda x: str(x).split(','))

    df1 = df1.explode("characters", ignore_index=True)
    df1['tconst'] = df1['tconst'].str[2:]
    df1['nconst'] = df1['nconst'].str[2:]

    df1 = df2.merge(df1, on='characters', how="inner")
    df1.dropna()
    df1.drop(['characters'], axis=1).to_csv('title_actor_character.csv', index=False)


