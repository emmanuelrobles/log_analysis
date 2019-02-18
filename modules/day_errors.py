import connection


def get_day_errors():

    conn = connection.Connection()

    db_cursor = conn.get_connection()

    querry = "SELECT * FROM " \
             "(SELECT OK.day,(cast((count_bad*100)as decimal)/(count_ok+count_bad)) as per" \
             " FROM " \
             "(SELECT date_trunc('day',time) as day, status, count(status) as count_ok FROM log WHERE status = '200 OK' group by 1,2) as OK " \
             "INNER JOIN (SELECT date_trunc('day',time) as day, status, count(status) as count_bad FROM log WHERE status != '200 OK' group by 1,2) as BAD " \
             "ON OK.day = BAD.day) " \
             "AS inner_table " \
             "WHERE per>1;"

    db_cursor.execute(querry)
    result = db_cursor.fetchall()
    del db_cursor

    return result

print get_day_errors()