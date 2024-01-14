#!/usr/bin/python3
""" filter states from states table """
import MySQLdb
import sys


def list_cities():
    """ filter states by it's name and avoid sql injection """

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM cities ORDER BY cities.id ASC"
    cursor.execute(query)

    for record in cursor.fetchall():
        print(record)


if __name__ == '__main__':
    list_cities()
