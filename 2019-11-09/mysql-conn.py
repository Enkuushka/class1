import mysql.connector

mysqlConn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="class",
    passwd=""
)

mysqlCursor = mysqlConn.cursor()

# mysqlCursor.execute("SELECT * from orders")

# data = mysqlCursor.fetchall()

# for row in data:
#     print(row)

in_id = int(input("ID: "))
in_name = str(input("Name: "))
in_phone = str(input("Phone: "))
in_gender = str(input("Gender /f, m/: "))

query = ("INSERT INTO people VALUES (%d, \"%s\", \"%s\", '%s')")%(in_id, in_name, in_phone, in_gender)

mysqlCursor.execute(query)
