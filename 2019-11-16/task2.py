import mysql.connector

mysqlConn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="class_db",
    passwd=""
)

def executeSql(query):
    mysqlCursor = mysqlConn.cursor()

    mysqlCursor.execute(query)

    data = mysqlCursor.fetchall()

    return data


songolt_1 = input("Унших[u], Бичих[b]: ")

if(songolt_1 == "u"):
    
    pass

elif(songolt_1 == "b"):
    print("Бичих хэрэглэгчээ сонго:")
    workers = executeSql("SELECT id, name FROM worker")
    for w in workers:
        print("[%d] %s"%(w[0], w[1]))
    
    w_id = input("Хэрэглэгчийн ID: ")
    
    print("Мэдээний ангилал сонго:")
    cats = executeSql("SELECT id, name FROM category")
    for row in cats:
        print("[%d] %s"%(row[0], row[1]))
    
    c_id = input("Хэрэглэгчийн ID: ")
    
    title = input("Мэдээний гарчиг: ")
    body = input("Мэдээ: ")

    pass
else:
    print("Буруу сонголт байна. Програм дууслаа.")