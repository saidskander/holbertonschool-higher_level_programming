#!/usr/bin/python3
"""Script that lists all states from database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == '__main__':
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               database=sys.argv[3])

    crsr = database.cursor()
    crsr.execute("SELECT cities.id, cities.name, states.name\
                  FROM cities\
                  LEFT JOIN states ON cities.state_id=states.id\
                  ORDER BY cities.id ASC")
    row = crsr.fetchall()
    for x in row:
        print(x)
    crsr.close()
    database.close()
