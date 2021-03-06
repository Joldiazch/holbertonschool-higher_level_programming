#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
if __name__ == '__main__':

    import MySQLdb
    """ For make querys to Mysql from python """
    from sys import argv
    """ For use argv """

    if len(argv) == 4:
        db = MySQLdb.connect(
            host="localhost",
            port=3306, user=argv[1],
            passwd=argv[2],
            db=argv[3])

        cur = db.cursor()
        cur.execute("""
        SELECT c.id, c.name, s.name
        FROM cities c
            INNER JOIN states s
                ON c.state_id = s.id
        ORDER BY id ASC;
        """)
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

        cur.close()
        db.close()
