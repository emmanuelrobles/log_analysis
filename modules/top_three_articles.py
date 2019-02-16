import connection


def get_top_three_articles():

    conn = connection.Connection()

    db_cursor = conn.get_connection()

    db_cursor.execute("SELECT path, count(*) as count FROM log where status = '200 OK' group by (path) order by count desc")

    print db_cursor.fetchall()

get_top_three_articles()