import connection


def get_top_authors():

    # create a connection
    conn = connection.Connection()
    # get the cursor
    db_cursor = conn.get_connection()

    path_folder = "/article/"
    # query to be run
    query = "SELECT name,count(*) " \
             "FROM articles " \
             "INNER JOIN log ON articles.slug = substring(log.path,length('/article/')+1) " \
             "INNER JOIN authors on author = authors.id " \
             "GROUP BY name " \
             "ORDER BY count DESC;".format(path_folder)

    # execute the query
    db_cursor.execute(query)
    # result will hold the results of the query
    result = db_cursor.fetchall()
    # close the connection
    del db_cursor

    return result