import connection


def get_day_errors():
    # create a connection
    conn = connection.Connection()
    # get the cursor
    db_cursor = conn.get_connection()

    # query to be run
    query = "SELECT * FROM " \
            "(SELECT OK.day,(cast((count_bad*100)as decimal)/(count_ok+count_bad)) as per" \
            " FROM " \
            "(SELECT date_trunc('day',time) as day, status, count(status) as count_ok FROM log WHERE status = '200 OK' group by 1,2) as OK " \
            "INNER JOIN (SELECT date_trunc('day',time) as day, status, count(status) as count_bad FROM log WHERE status != '200 OK' group by 1,2) as BAD " \
            "ON OK.day = BAD.day) " \
            "AS inner_table " \
            "WHERE per>1;"

    # execute the query
    db_cursor.execute(query)
    # result will hold the results of the query
    result = db_cursor.fetchall()
    # close the connection
    del db_cursor

    return result
