#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get the MySQL credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=db_name,
        port=3306
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all states, sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results and print them
    states = cur.fetchall()
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cur.close()
    db.close()

