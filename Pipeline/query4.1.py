import pymongo
import matplotlib.pyplot as plt
import pandas as pd

# pymongo connection by passing the connection string
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["hw4"]
collection = db["Movies"]
pipeline = [
    {
        "$match": {
            "numVotes": {"$gt": 10000},
        }
    },
    {
        "$unwind": "$genre"
    }
]
# we pass the pipeline to the result_list and the whole type is of list
result_list = list(collection.aggregate(pipeline))
# putting the result_list in a dataframe
result_df = pd.DataFrame(result_list)
# exploding on genre to get each genre
result_df = result_df.explode('genre')
# box plot on the avg rating by genre
result_df.boxplot(column='avgRating', by='genre', rot=90)
plt.title(f"Movie genres with votes greater than 10000")
plt.show()

