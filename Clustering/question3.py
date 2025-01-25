import math
from statistics import mean
import numpy as np
import pandas as pd
import pymongo

# mongo connection
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["hw4"]
movies_norm_collection = db["movies_norm"]
centroid_collection = db["centroid"]

g = "Action"

# pipepline
pipeline = [
    {
        "$unwind": "$genre"
    },
    {
        "$match": {
            "genre": g
        }
    }
]

# creating lists
movie_norm_list = list(movies_norm_collection.aggregate(pipeline))
centroid_list = list(centroid_collection.find({}))

# creating dataframes
movie_norm_df = pd.DataFrame(movie_norm_list)
centroid_df = pd.DataFrame(centroid_list)

# creating a new field and setting the values to nan
movie_norm_df['cluster'] = np.nan

# looping through the movie norm df
for index, row in movie_norm_df.iterrows():
    # setting min distance to infinity
    min_distance = float('inf')
    cluster_id = 0
    # looping through the centroid dataframe
    for index2, centroid in centroid_df.iterrows():
        # finding the eucledian distance
        eDistance = math.dist(row['kmeansNorm'], centroid['kmeansNorm'])
        # insert if the distance is less than min distance
        if eDistance < min_distance:
            min_distance = eDistance
            cluster_id = centroid['ID']
    # assigning the id
    movie_norm_df.loc[index, 'cluster'] = cluster_id

# looping through the centroid dataframe
for index2, centroid in centroid_df.iterrows():
    # getting the data
    temp_df = movie_norm_df[movie_norm_df['cluster'] == centroid['ID']].copy()
    temp_df[['x', 'y']] = temp_df.kmeansNorm.tolist()
    # finding the mean of x and y
    x = mean(temp_df.x.tolist())
    y = mean(temp_df.y.tolist())
    centroid_df.at[index2, 'kmeansNorm'] = [x, y]
    # updating the centroid collection
    centroid_collection.update_one({'ID': centroid['ID']}, {"$set": {"kmeansNorm": [x, y]}})