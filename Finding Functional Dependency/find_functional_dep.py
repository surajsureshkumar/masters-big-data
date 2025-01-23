import pandas as pd
from itertools import combinations

relation = pd.read_csv('find_dependencies.tsv', sep='\t')

for column in relation.columns:  # selecting column from the dataframe
    for column_length in range(1, len(relation.columns)):  # looping till the length of the columns in dataframe
        # combinations of the columns which takes upto the length of the j which is specified by r
        for column_combination in combinations(list(relation.columns),
                                               r=column_length):

            # if column 1 in combinations then continue because we want to remove the column
            if column in column_combination:
                continue

            cols = list(column_combination)  # appending the column from c into a list and storing it in a variable
            cols.append(column)  # appending the column to cols since that is unique
            column_set = set(relation[
                        column])  # creating a set and removing duplicate values for the column mentioned by relation[i]

            # then for all the columns in cols we are dropping the duplicates
            column_list_set = relation[cols].drop_duplicates()

            # if len of column_set and column_list_set are equal then print the dependency
            if len(column_set) == len(column_list_set):
                print(column, "-->", column_combination)

