# masters-big-data
This repository contains the code and resources for my master's-level Big Data assignment. The project explores concepts of distributed data processing, scalability, and data analytics

Overview
The data.py script in Pre-Processing performs preprocessing tasks, such as cleaning and transforming data fields, to prepare the data for further analysis.

## Dataset
All data files required for this assignment are available from the IMDB Non-Commercial Datasets https://developer.imdb.com/non-commercial-datasets/. 

## How to Run the Assignment1

### Prerequisites
Make sure to have Python: Version 3.8 or higher

### Libraries:
Install the required Python libraries by running:
`pip install pandas numpy`

### Download the Dataset
Visit the IMDB Non-Commercial Datasets page.
Download all the required data files.
Place the downloaded file in the same directory as your python script.

### Run the Script
Run the data.py script from the terminal using the following command:
`python3 <FILE_NAME>.py`

### Expected Output
The script in Pre-Processing performs the following tasks:
Reads the title.ratings.tsv.gz file into a Pandas DataFrame.
Cleans and transforms specific fields in the dataset (e.g., removing prefixes from IDs).
Prepares the data for further analysis.

### The script in Pre-Processing performs the following tasks:

`title(): Merges the title.basics.tsv.gz and title.ratings.tsv.gz files to prepare a combined dataset with movie information and ratings, saving the result as title.csv.
genre(): Extracts and counts the unique genres from the title.basics.tsv.gz file, and saves the result as genres.csv.
member(): Processes the name.basics.tsv.gz file to clean up and store member (actor/actress/producer) details in member.csv.
characters(): Extracts and cleans character names from the title.principals.tsv.gz file, storing the unique characters in characters.tsv.
title_actor(): Processes the title.principals.tsv.gz file to extract the relationship between titles and actors/actresses, saving it as title_actor.tsv.
title_writers(): Extracts and processes writer information from the title.crew.tsv.gz file, saving the cleaned data in title_writers.csv.
title_director(): Extracts and processes director information from the title.crew.tsv.gz file, saving the cleaned data in title_directors.csv.
title_producer(): Extracts and processes producer information from the title.principals.tsv.gz file, saving the cleaned data in title_producer.csv.
title_actor_character(): Combines data from title.principals.tsv.gz and characters.tsv to create a detailed relationship between actors and characters, saving the result in title_actor_character.csv`
