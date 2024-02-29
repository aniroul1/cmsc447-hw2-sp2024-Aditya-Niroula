import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table with 3 fields: name, id, and points
cursor.execute('''CREATE TABLE IF NOT EXISTS PLAYERS(
                  Name TEXT NOT NULL,
                  ID INTEGER PRIMARY KEY,
                  Points INTEGER NOT NULL)''')

# Commit the changes and close the connection
conn.commit()
conn.close()
