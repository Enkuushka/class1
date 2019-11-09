import sqlite3

conn = sqlite3.connect('sqlite-db-name.db')

myCursor = conn.cursor()

try:
    myCursor.execute('''CREATE TABLE people
            (id integer, name text, phone text)''')
except:
    pass



conn.commit()
conn.close()