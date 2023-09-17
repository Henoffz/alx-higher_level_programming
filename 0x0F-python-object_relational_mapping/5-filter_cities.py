#!/usr/bin/python3
"""
script that lists all cities from the database
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
        )
    state_name = argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 LEFT JOIN states\
                 ON states.id = cities.state_id\
                 WHERE states.name LIKE BINARY (%s) ORDER BY cities.id ASC",
                (state_name,))
    rows = cur.fetchall()

    city_names = ", ".join(row[0] for row in rows)
    print(city_names)

    cur.close()
    db.close()
