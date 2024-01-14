#!/usr/bin/python3
""" filter states from states table """
import MySQLdb
import sys


def filter_states_by_name():
    """ filter states by it's name """

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states \
WHERE name = "{}" ORDER BY states.id ASC'.format(sys.argv[4]))

    for record in cursor.fetchall():
        print(record)


if __name__ == '__main__':
    filter_states_by_name()
