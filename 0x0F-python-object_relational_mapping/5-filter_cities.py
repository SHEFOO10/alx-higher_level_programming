#!/usr/bin/python3
""" filter states from states table """
import MySQLdb
import sys


def list_cities_on_specfic_state():
    """ list cities in specific state and avoid sql injection """

    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    query = """ SELECT cities.name FROM states \
                JOIN cities ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %s
                ORDER BY cities.id ASC """
    cursor.execute(query, (sys.argv[4],))

    # for record in cursor.fetchall():
    print(', '.join([city[0] for city in cursor.fetchall()]))

if __name__ == '__main__':
    list_cities_on_specfic_state()