#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
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
        cursor.execute("SELECT cities.name FROM cities, states\
                       WHERE cities.state_id=states.id AND states.name = %s\
                       ORDER BY cities.id ASC;", (sys.argv[4],))
        print(", ".join(["{}".format(row[0]) for row in cursor.fetchall()]))
        cursor.close()
        db.close()
