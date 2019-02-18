import connection


def get_top_three_articles():

    conn = connection.Connection()

    db_cursor = conn.get_connection()

    path_folder = "/article/"

    querry = "SELECT title, count(*) as count FROM articles " \
             "INNER JOIN log ON articles.slug = substring(log.path,LENGTH ('{0}')+1) " \
             "GROUP BY title " \
             "order by count desc " \
             "LIMIT 3;".format(path_folder)

    db_cursor.execute(querry)
    result = db_cursor.fetchall()
    del db_cursor
    return result