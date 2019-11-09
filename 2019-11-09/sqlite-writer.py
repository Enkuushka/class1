import sqlite3

conn = sqlite3.connect('sqlite-db-name.db')

myCursor = conn.cursor()

try:
    myCursor.execute('''INSERT INTO cars VALUES
                    (1, "Bat", "6655"),
                    (2, "Damba", "1122")''')
except:
    print("Aldaa")


conn.commit()
conn.close()