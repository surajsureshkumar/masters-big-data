import time

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, array_contains

spark = SparkSession.builder.getOrCreate()

dataframe = spark.read.csv('name.basics (1).tsv.gz', sep='\t', header=True, inferSchema=True)
dataframe2 = spark.read.csv('title.basics.tsv.gz', sep='\t', header=True, inferSchema=True)
dataframe3 = spark.read.csv('title.principals (1).tsv.gz', sep='\t', header=True, inferSchema=True)

df1 = dataframe.join(dataframe3, on="nconst", how="inner")
final_df = df1.join(dataframe2, on="tconst", how="inner")
final_df = final_df.filter(final_df.isAdult == 0)

# query 1
start_time = time.time()
query1 = final_df.filter(
    (col("deathYear") == "\\N") & (col("primaryName").startswith("Phi")) & (col("titleType") == "movie")
    & (col("startYear") != 2014)).select("primaryName")
query1.show(10)
elapsed_time = time.time() - start_time
print('Time taken to run the query', elapsed_time)

# query 2
start_time = time.time()
genre_array = final_df.withColumn("genres", split(final_df.genres, ","))
query2 = genre_array.filter(
    (col("category") == "producer") & (col("primaryName").contains("Gill")) & (col("startYear") == 2017) & (
        array_contains(genre_array.genres, "Talk-Show"))).groupBy(
    "primaryName").count().sort(col('count').desc())
query2.show(10)
elapsed_time = time.time() - start_time
print('Time taken to run the query', elapsed_time)

# query 3
start_time = time.time()
query3 = final_df.filter(
    (col("category") == "producer") & (col("runtimeMinutes") > 120) & (col("deathYear") == "\\N")).groupBy(
    "primaryName").count().sort(col('count').desc())
query3.show(10)
elapsed_time = time.time() - start_time
print('Time taken to run the query', elapsed_time)

# query 4
start_time = time.time()
query4 = final_df.filter(
    (col("deathYear") == "\\N") & ((col("category") == "actor") | (col("category") == "actress")) &
    ((col("characters").contains("Jesus")) | (col("characters").contains("Christ")))).select("primaryName").distinct()
query4.show(10)
elapsed_time = time.time() - start_time
print('Time taken to run the query', elapsed_time)
