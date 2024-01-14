#!/usr/bin/python3
""" filter states from states table """
import MySQLdb
import sys


def filter_states():
    """ filter states from database """

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states \
        WHERE name LIKE BINARY "N%" ORDER BY states.id ASC')
    for record in cursor.fetchall():
        print(record)


if __name__ == '__main__':
    filter_states()
