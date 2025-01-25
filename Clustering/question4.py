import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymongo
import random
from statistics import mean

# mongo connection
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["hw4"]
movies_norm_collection = db["movies_norm"]
centroid_collection = db["centroid"]

# defining the genres
genres = ['Action', 'Horror', 'Romance', 'Sci-Fi', 'Thriller']
g = "Action"


def kmeans(movie, number_of_clusters, number_of_iter):
    """
    Kmeans function
    :param movie: the data
    :param number_of_clusters: the number of clusters
    :param number_of_iter: the number of times to iterate
    :return: centroids
    """
    centroids = random.sample(movie['kmeansNorm'].tolist(), number_of_clusters)  # creating the number of centroids
    print(number_of_clusters)
    # looping through the number of iterations
    for i in range(number_of_iter):
        print(i, end=" ")
        # looping through the movie
        for index, row in movie.iterrows():
            min_distance = float('inf')
            cluster_id = 0
            # computing the eucledian distance
            for index2, centroid in enumerate(centroids):
                eDistance = math.dist(row['kmeansNorm'], centroid)
                if eDistance < min_distance:
                    min_distance = eDistance
                    cluster_id = index2 + 1
            movie.loc[index, 'cluster'] = cluster_id
        centroid_lst = []  # list to store the centroids
        # looping through the centroids created
        for index, centroid in enumerate(centroids):
            temp_df = movie[movie['cluster'] == index + 1].copy()
            value = [doc[0] for doc in temp_df.kmeansNorm.tolist()]
            value2 = [doc[1] for doc in temp_df.kmeansNorm.tolist()]
            x, y = centroid
            # if the length is not equal to 0 then find the mean
            if len(value) != 0:
                x = mean(value)
            # if the length is not equal to 0 then find the mean
            if len(value2) != 0:
                y = mean(value2)
            # appending x and y to the centroid list
            centroid_lst.append([x, y])
        if centroids == centroid_lst:
            return centroids
        else:
            centroids = centroid_lst
    return centroids


def main():
    """
    Main Function
    :return:
    """
    # looping through the genres
    for genre in genres:
        print(genre)
        # pipeline
        pipeline = [
            {
                "$unwind": "$genre"
            },
            {
                "$match": {
                    "genre": genre
                }
            }
        ]
        # movie norm list and dataframe
        movie_norm_list = list(movies_norm_collection.aggregate(pipeline))
        movie_norm_df = pd.DataFrame(movie_norm_list)

        # creating a new field cluster and assigning it none
        movie_norm_df['cluster'] = np.nan
        sse = []  # list to squared error
        for k in range(10, 51, 5):
            # calling the kmeans function
            centroid = kmeans(movie_norm_df, k, 100)
            squared_error = []
            # looping through the centroids
            for index, center in enumerate(centroid):
                temp_df = movie_norm_df[movie_norm_df['cluster'] == index + 1].copy()
                # appending the value to the squared error
                squared_error.append(sum([math.dist(a, center) for a in temp_df.kmeansNorm.tolist()]))
            sse.append([k, sum(squared_error)])
            print("\n{}".format(sse))
        # assinging the values to x and y to plot
        y = [point[1] for point in sse]
        x = [point[0] for point in sse]

        # plotting the graph
        plt.plot(x, y)
        plt.xlabel('Clusters')
        plt.ylabel('Sum of squared errors ')
        plt.show()


if __name__ == '__main__':
    main()
