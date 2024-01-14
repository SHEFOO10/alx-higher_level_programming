#!/usr/bin/python3
import MySQLdb, sys

db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()

cursor.execute('SELECT * FROM states ORDER BY states.id')
for record in cursor.fetchall():
    print(record)