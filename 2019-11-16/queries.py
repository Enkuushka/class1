import mysql.connector

mysqlConn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="class_db",
    passwd=""
)

mysqlCursor = mysqlConn.cursor()

query1 = "SELECT start_year FROM worker WHERE address='UB3'"

mysqlCursor.execute(query1)

data = mysqlCursor.fetchone()

print(data[0])

query2 = '''
        SELECT w.name, count(*) as too FROM orders as o
        JOIN worker as w ON w.id = o.worker_id
        WHERE w.start_year = 2002
        GROUP BY w.name
'''

mysqlCursor.execute(query2)

data = mysqlCursor.fetchall()

print(data)