import connection


def get_top_three_articles():

    db_cursor = connection.Connection.get_connection()

    db_cursor.execute("SELECT * FROM articles")

    print db_cursor.fetchall()