#!/usr/bin/python3
import MySQLdb
import sys
connect = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2],
        database=sys.argv[3], port=3306
)
cursor = connect.cursor()
cursor.execute(
        """SELECT cities.id, cities.name, state.name
        FROM cities
        INNER JOIN states ON states.id=cities.state_id
        ORDER BY cities.id ASC;
        """
)
for row in cursor:
    print(row)
cursor.close()
connect.close()
