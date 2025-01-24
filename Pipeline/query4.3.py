import pymongo
import matplotlib.pyplot as plt
import pandas as pd

# connecting to the mongo database where the connection string is given to the client and selecting the database
# and the collection
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["hw4"]
collection = db["Movies"]
# Below is the query which has been stored in the pipeline
pipeline = [
    {
        "$group": {
            "_id": "$startYear",
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"_id": 1}
    }
]
# we pass the pipeline to the result_list and the whole type is of list
result_list = list(collection.aggregate(pipeline))

# putting the result_list in a dataframe
result_df = pd.DataFrame(result_list)

# converting to date time and setting index and then plotting the result_df and xlabel and ylabel is mentioned
result_df["_id"] = pd.to_datetime(result_df["_id"], format="%Y")
result_df.set_index("_id", inplace=True)
plt.plot(result_df)
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.title("Number of Movies Produced Each Year")
plt.show()
