import psycopg2


class Connection:

    # initialize the connection
    def __init__(self):
        self.db = psycopg2.connect("dbname=news")

    # return the cursor
    def get_connection(self):
        return self.db.cursor()

    # close the connection
    def __del__(self):
        self.db.close()
