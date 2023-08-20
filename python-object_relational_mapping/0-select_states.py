#!/usr/bin/python3
"""this script connect to MYSQL server, list all state from the database hbtn_0e_0_usa, it takes 3 argument"""
import MySQLdb
import sys
connect = MySQLdb.connect(host='localhost', user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)
cursor = connect.cursor()
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)
cursor.close()
connect.close()
