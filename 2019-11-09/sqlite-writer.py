import sqlite3

conn = sqlite3.connect('sqlite-db-name.db')

myCursor = conn.cursor()

myCursor.execute('''INSERT INTO people VALUES
                    (1, "Bat", "6655"),
                    (2, "Damba", "1122")''')


conn.commit()
conn.close()