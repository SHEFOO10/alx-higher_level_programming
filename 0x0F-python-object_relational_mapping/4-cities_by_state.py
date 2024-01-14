#!/usr/bin/python3
""" list cities table """
import MySQLdb
import sys


def list_cities():
    """ list all cities records """

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities, states
    WHERE states.id = cities.state_id ORDER BY cities.id ASC """
    cursor.execute(query)

    for record in cursor.fetchall():
        print(record)


if __name__ == '__main__':
    list_cities()
