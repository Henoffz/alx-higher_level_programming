#!/usr/bin/python3
"""
 script that takes in arguments and displays all values
 in the states table of hbtn_0e_0_usa where name
 matches the argument
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
    cur.execute("SELECT * FROM states WHERE name = (%s)\
    ORDER BY states.id ASC", (state_name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
