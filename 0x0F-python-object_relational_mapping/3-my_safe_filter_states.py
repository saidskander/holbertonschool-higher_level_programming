#!/usr/bin/python3
"""Script that lists all states from database hbtn_0e_0_usa"""
import MySQLdb
import sys


def filter_names_safe():
    """argv arguments to list from SQL_database
       username, password, name, state name searched.
    """

    if len(sys.argv) == 6:
        database = MySQLdb.connect(host="localhost",
                                   port=3306,
                                   user=sys.argv[1],
                                   passwd=sys.argv[2],
                                   database=sys.argv[3])

        crsr = database.cursor()
        crsr.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                     ORDER BY id ASC".format(sys.argv[4]))
        row = crsr.fetchall()
        for x in row:
            print(x)

       crsr.close()
       database.close()
    else:
        return

if __name__ == "__main__":
    filter_names_safe():
