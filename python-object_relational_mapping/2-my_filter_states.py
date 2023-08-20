#!/usr/bin/python3
import MySQLdb
import sys
connect = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2],
        database=sys.argv[3], port=3306
)
name = sys.argv[4]
input_name = input("Enter a state name: ")
cursor = connect.cursor()
query = "SELECT * FROM states WHERE name LIKE '{}%' ORDER BY id ASC".format(input_name)
cursor.execute(query)
for obj in cursor:
    print(obj)
cursor.close()
connect.close()
