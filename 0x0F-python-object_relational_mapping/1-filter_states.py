#!/usr/bin/python3
import MySQLdb
from sys import argv
""" For use argv and For make querys to Mysql from python """

if __name__ == '__main__':

    if len(argv) == 4:
        db = MySQLdb.connect(
            host="localhost",
            port=3306, user=argv[1],
            passwd=argv[2],
            db=argv[3])

        cur = db.cursor()
        cur.execute("""
        SELECT *
        FROM states
        WHERE name REGEXP BINARY '^(N)'
        ORDER BY id ASC
        """)
        query_rows = cur.fetchall()

        for row in query_rows:
            if row
            print(row)
        cur.close()
        db.close()
