import psycopg2

# database connection
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="hw2",
    user="postgres",
    password="surajsuri1456@#$"
)
cur = conn.cursor()

# minimum support and the current level from which we start
min_support = 5
current_level = 2

while True:
    # query string
    query1 = 'CREATE TABLE L{} AS SELECT '.format(current_level)

    # looping till the level and using the format to the add the desired text
    for level in range(1, current_level):
        query1 += 'a.actor{},'.format(level)

    # concatenating to the query1
    query1 += 'b.actor{} as actor{}, COUNT(*) AS count FROM '.format(current_level - 1, current_level)
    for alias in ['a', 'b']:
        query1 += 'public.l{} {},'.format(current_level - 1, alias)

    # making sure that the comma is not added to the last line of the query that is concatenated by this for loop
    for alias in range(current_level):
        query1 += 'public.popular_movie_actors pma{}'.format(alias + 1)
        if alias != current_level - 1:
            query1 += ','
    query1 += ' WHERE '

    for alias in range(1, current_level):
        query1 += 'a.actor{} = pma{}.actor and '.format(alias, alias)

    query1 += 'b.actor{} = pma{}.actor and '.format(current_level - 1, current_level)

    for alias in range(1, current_level - 1):
        query1 += 'a.actor{} = b.actor{} and '.format(alias, alias)
    query1 += 'a.actor{} < b.actor{} and '.format(current_level - 1, current_level - 1)

    # making sure that the and is not added to the last line of the query that is concatenated by this for loop
    for alias in range(1, current_level):
        query1 += 'pma{}.title = pma{}.title'.format(alias, alias + 1)
        if alias != current_level - 1:
            query1 += ' and '

    query1 += ' GROUP BY '

    for alias in range(1, current_level):
        query1 += 'a.actor{}, '.format(alias)
    query1 += 'b.actor{}'.format(current_level - 1)
    query1 += ' HAVING COUNT(*) >= {};'.format(min_support)
    # executing the query and commiting the changes after it is executed to the database
    cur.execute(query1)
    conn.commit()
    # fetching all the records and executing the query
    query2 = 'SELECT * from l{}'.format(current_level)
    cur.execute(query2)

    number_of_records = len(cur.fetchall())  # getting the len of the records
    # if the length of the records is 0 then we break
    if number_of_records == 0:
        break
    else:
        # else we print each level and the number of records
        print('Level {} = {}'.format(current_level, number_of_records))
        current_level += 1

# closing the connection
cur.close()
conn.close()
