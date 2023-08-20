#!/usr/bin/python3
"""this script connect to MYSQL server, list all state from the database hbtn_0e_0_usa, it takes 3 argument"""
import MySQLdb

connect = MySQLdb.connect(host='localhost', user=mysql username, password=mysql password, database=database name, port=3306)
cursor = connect.cursor()
query = "SELECT id, name FROM states ORDER BY id ASC"
cursor.execute(query)
for row in cursor:
    print(row[0], row[1])
cursor.close()
connect.close()
