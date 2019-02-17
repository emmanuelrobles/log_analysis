import connection


def get_top_authors():

    conn = connection.Connection()

    db_cursor = conn.get_connection()

    path_folder = "/article/"

    querry = "SELECT name,count(*) " \
             "FROM articles " \
             "INNER JOIN log ON articles.slug = substring(log.path,length('/article/')+1) " \
             "INNER JOIN authors on author = authors.id " \
             "GROUP BY name " \
             "ORDER BY count DESC;".format(path_folder)

    db_cursor.execute(querry)

    return db_cursor.fetchall()