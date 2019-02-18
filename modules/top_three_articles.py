import connection


def get_top_three_articles():

    # create a connection
    conn = connection.Connection()
    # get the cursor
    db_cursor = conn.get_connection()

    path_folder = "/article/"
    # query to be run
    query = "SELECT title, count(*) as count FROM articles " \
             "INNER JOIN log ON articles.slug = substring(log.path,LENGTH ('{0}')+1) " \
             "GROUP BY title " \
             "order by count desc " \
             "LIMIT 3;".format(path_folder)

    # execute the query
    db_cursor.execute(query)
    # result will hold the results of the query
    result = db_cursor.fetchall()
    # close the connection
    del db_cursor

    return result