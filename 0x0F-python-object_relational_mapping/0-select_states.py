#!/usr/bin/python3
""" select states from states table """
import MySQLdb
import sys


def list_states():
    """ list states from database """

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')
    for record in cursor.fetchall():
        print(record)


if __name__ == '__main__':
    list_states()
