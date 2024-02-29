import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table with 3 fields: name, id, and points
cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
                  id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  points INTEGER NOT NULL)''')

# Commit the changes and close the connection
conn.commit()
conn.close()

