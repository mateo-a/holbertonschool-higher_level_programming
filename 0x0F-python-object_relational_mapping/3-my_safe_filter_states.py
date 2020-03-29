#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if (len(sys.argv) == 5):
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC;",
                       (sys.argv[4],))
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()
