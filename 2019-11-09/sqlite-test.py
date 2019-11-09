import sqlite3

conn = sqlite3.connect('sqlite-db-name.db')

myCursor = conn.cursor()

myCursor.execute('''CREATE TABLE people
             (id integer, name text, phone text)''')

conn.commit()
conn.close()