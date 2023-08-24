#!/usr/bin/python3
"""this script takes in the name of a state as an argument and lists all cities of that state"""
import MySQLdb
import sys
state_name = sys.argv[4]
connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
        password=sys.argv[2], port=3306, database=sys.argv[3])
cursor = connect.cursor()
cursor.execute("""
        SELECT cities.name 
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
        """) .format(state_name)
for row in cursor:
    print(row)
cursor.close()
connect.close()
