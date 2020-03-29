#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if (len(sys.argv) == 4):
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                       ORDER BY id ASC;")
        for row in cursor.fetchall():
            if ("N" in row[1]):
                print(row)
        cursor.close()
        db.close()
