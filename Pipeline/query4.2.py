import numpy as np
import pymongo
import matplotlib.pyplot as plt
import pandas as pd

# pymongo connection by passing the connection string
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["hw4"]
collection = db["movie"]
# Below is the query which has been stored in the pipeline
pipeline = [
    {"$unwind": "$actors"},
    {"$match": {"actors.actor": {"$ne": None}}},
    {"$group": {"_id": {
        "_id": "$_id",
        "genre": "$genre"
    }, "actor_count": {"$sum": 1}}},
    {"$unwind": "$_id.genre"},
    {"$group": {"_id": "$_id.genre",
                "averageActor": {"$avg": "$actor_count"}}},
    {"$match": {
        "_id": {
            "$ne": "\\N"
        }
    }}
]
# we pass the pipeline to the result_list and the whole type is of list
result_list = list(collection.aggregate(pipeline))
result_df = pd.DataFrame(result_list)
# plotting the bar graph
result_df.plot.bar(x="_id", y="averageActor")
plt.xlabel('genre')
plt.ylabel('average number of actors')
plt.show()
