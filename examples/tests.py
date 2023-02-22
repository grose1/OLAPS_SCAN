import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("D:\\pyhon projects\\OLAPS_SCAN\\database\\test.db")

cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM top10;'):
    print(row)

# Be sure to close the connection
con.close()