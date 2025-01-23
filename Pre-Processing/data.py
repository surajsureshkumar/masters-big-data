"""
CSCI-620: Assignment 1
Author: Suraj Sureshkumar (ss7495@g.rit.edu)

"""
import numpy as np
import pandas as pd


def ratings():
    """
    Preprocessing the title.ratings.tsv.gz
    :return: None
    """

    tsv_file = "title.ratings.tsv.gz"  # storing the file to a variable

    df = pd.read_table(tsv_file)  # using pd.read_table to read delimited file into dataframe

    df['tconst'] = df['tconst'].apply(
        lambda x: x.split('t')[
            -1])  # removing the tt from tconst, splitting on t and taking out the last value of the list
    df.to_csv('ratings.csv', index=False)  # converting the dataframe to a csv file where index is ignored


def movie_title():
    """
    Pre-processing the title.basics.tsv.gz
    :return: None
    """
    tsv_file = "title.basics.tsv.gz"  # storing the file to a variable

    df = pd.read_table(tsv_file)  # using pd.read_table to read delimited file into dataframe

    df['tconst'] = df['tconst'].apply(
        lambda x: x.split('t')[
            -1])  # removing the tt from tconst, splitting on t and taking out the last value of the list
    df.drop(['isAdult', 'startYear', 'endYear', 'genres'], axis=1).to_csv('movie_title.csv',
                                                                          index=False)  # dropping the attributes
    # which are not relevant in generating the particular csv which is associated with the table created and
    # converting the dataframe to csv file


def episodes():
    """
    Pre-processing the title.episode.tsv.gz
    :return: None
    """
    tsv_file = "title.episode.tsv.gz"  # storing the file to a variable

    df = pd.read_table(tsv_file)  # using pd.read_table to read delimited file into dataframe

    df['tconst'] = df['tconst'].apply(lambda x: x.split('t')[
        -1])  # removing the tt from tconst, splitting on t and taking out the last value of the list
    df['parentTconst'] = df['parentTconst'].apply(lambda x: x.split('t')[
        -1])  # removing the tt from tconst, splitting on t and taking out the last value of the list
    df.replace(r'\N', np.NaN, inplace=True)  # replacing the \N with NaN

    df.to_csv('episode.csv', index=False)  # converting the dataframe to csv


def crew():
    """
    Preprocessing the name.basics.tsv.gz and title.principals.tsv.gz
    :return:
    """
    tsv_file1 = "name.basics.tsv.gz"
    tsv_file2 = "title.principals.tsv.gz"

    # using pd.read_table to read delimited file into dataframe
    df1 = pd.read_table(tsv_file1)  # Dataframe 1
    df2 = pd.read_table(tsv_file2)  # Dataframe 2

    df1['nconst'] = df1['nconst'].str[2:]  # reading the string from the 2nd character and ignoring the first two
    df2['tconst'] = df2['tconst'].str[2:]  # reading the string from the 2nd character and ignoring the first two
    df2['nconst'] = df2['nconst'].str[2:]  # reading the string from the 2nd character and ignoring the first two

    df1 = pd.merge(df1, df2, on="nconst")  # merging the two dataframe of df1 and df2 on nconst
    df1.replace(r'\N', np.NaN, inplace=True)  # replacing the \N with NaN

    df1.to_csv('crew.csv', index=False)  # converting the dataframe to csv


def regional_title():
    """
    Pre-processing the title.akas.tsv.gz
    :return: None
    """
    tsv_file = "title.akas.tsv.gz"

    df = pd.read_table(tsv_file)  # using pd.read_table to read delimited file into dataframe

    df['titleId'] = df['titleId'].apply(
        lambda x: x.split('t')[-1])  # reading the string from the 2nd character and ignoring the first two
    df.replace(r'\N', np.NaN, inplace=True)  # replacing the \N with NaN

    # converting to csv file
    df[['titleId', 'ordering', 'language', 'region', 'title', 'isOriginalTitle']].to_csv("regional_title.csv",
                                                                                         index=False)


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


def movie_genre_mapping():
    """
    Mapping the movie_title(tconst) and the genre(genre_id)
    :return: None
    """
    tsv_file1 = "title.basics.tsv.gz"
    tsv_file2 = "genres.csv"

    # using pd.read_table to read delimited file into dataframe and reading only 2 columns
    df1 = pd.read_table(tsv_file1, usecols=["tconst",
                                            "genres"])
    df1["genres"] = df1['genres'].str.split(',')  # splitting on the genres
    df1 = df1.explode("genres", ignore_index=True)  # converting each element of the genres into a row using explode
    df2 = pd.read_csv(tsv_file2, header=0)  # second data frame which reads the second file

    genre_dict = {}  # initializing an empty dictionary

    # looping through the index and row of the dataframe 2
    for index, row in df2.iterrows():
        genre_dict[row['genres']] = row['genre_id']  # assigning each genres to their respective ids
    df1.replace({"genres": genre_dict}, inplace=True)  # replacing each genre with their id
    df1['tconst'] = df1['tconst'].str[2:]

    df1.to_csv('movie_genre_mapping.csv', index=False)  # converting to csv file


def movie_title_crew_mapping():
    """
    Pre-processing of title.principals.tsv.gz
    :return: None
    """
    tsv_file = "title.principals.tsv.gz"

    df = pd.read_table(tsv_file)  # using pd.read_table to read delimited file into dataframe

    df['tconst'] = df['tconst'].str[2:]  # reading the string from the 2nd character and ignoring the first two
    df['nconst'] = df['nconst'].str[2:]  # reading the string from the 2nd character and ignoring the first two

    # dropping the unnecessary attributes and creating the csv file
    df.drop(['job', 'characters'], axis=1).to_csv('movie_title_crew_mapping.csv', index=False)


def main():
    """
    Executed them one by one and commenting out others
    :return: None
    """
    ratings()
    movie_title()
    episodes()
    crew()
    regional_title()
    genre()
    movie_genre_mapping()
    movie_title_crew_mapping()


if __name__ == '__main__':
    main()
