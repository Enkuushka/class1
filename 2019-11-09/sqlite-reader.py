import sqlite3

conn = sqlite3.connect('sqlite-db-name.db')

myCursor = conn.cursor()

data = myCursor.execute('''SELECT * FROM people''')

for one_row in data:
    print(one_row)

conn.commit()
conn.close()