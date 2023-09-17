#!/usr/bin/python3
"""
script that lists all states from the database
hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
