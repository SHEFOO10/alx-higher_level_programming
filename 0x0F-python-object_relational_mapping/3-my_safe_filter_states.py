#!/usr/bin/python3
""" filter states from states table """
import MySQLdb
import sys


def safe_filter_states():
    """ filter states by it's name and avoid sql injection """

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states \
WHERE name LIKE BINARY %s ORDER BY states.id ASC"
    cursor.execute(query, (sys.argv[4],))

    for record in cursor.fetchall():
        print(record)


if __name__ == '__main__':
    safe_filter_states()
