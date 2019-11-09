# 1. Сурагч бүртгэх, дараах мэдээллүүдийг гараас өгнө:
#  - Id
#  - Нэр
#  - Төрсөн огноо
#  - Анги
# ӨС-руу бичнэ.

import sqlite3

conn = sqlite3.connect('suragch-db.db')

myCursor = conn.cursor()

try:
    myCursor.execute('''CREATE TABLE suragch
            (id integer, name text, phone text)''')
except:
    pass



# TODO



conn.commit()
conn.close()