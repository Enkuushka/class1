import mysql.connector
import datetime

mysqlConn = mysql.connector.connect(
    host="localhost", # 192.168.1.155
    user="root",
    database="class_db",
    passwd=""
)

def executeSql(query):
    mysqlCursor = mysqlConn.cursor()

    mysqlCursor.execute(query)

    if(mysqlCursor.with_rows):
        data = mysqlCursor.fetchall()
        return data
    
    return "OK"


songolt_1 = input("Унших[u], Бичих[b]: ")

if(songolt_1 == "u"): 

    query = '''SELECT id, title FROM content
    ORDER BY id DESC, created_date DESC
    LIMIT 5'''

    data = executeSql(query)
    for row in data:
        print("[%d] %s"%(row[0], row[1]))

    content_id = int(input("Мэдээний ID: "))

    query = '''SELECT * FROM content
    WHERE id = %d'''%(content_id)

    news = executeSql(query)
    old_viewed_count = news[0][5]
    query = '''UPDATE content
    SET viewed_count = %d
    WHERE id = %d'''%(old_viewed_count+1, content_id)
    executeSql(query)
    print(news[0][1])
    print("--------------")
    print(news[0][2])

    print("[L]ike    [C]omment")
    action = input(": ")
    
    if(action == "L"):
        old_like_count = news[0][6]
        query = '''UPDATE content
        SET like_count = %d
        WHERE id = %d'''%(old_like_count+1, content_id)
        executeSql(query)
        print("Liked!")

    elif(action == "C" or action == "c"):
        guest_name = input("Таны нэр: ")
        comment = input("Сэтгэгдэл: ")

        max_id = executeSql("SELECT MAX(IFNULL(id, 0)) FROM comments")
        print(max_id)
        newid = max_id[0][0]+1
        query = '''INSERT INTO comments (id, name, body, content_id)
            VALUES
            (%d, "%s", "%s", %d)
            '''%(newid, guest_name, comment, content_id)
        executeSql(query)
        print("Commented!")


elif(songolt_1 == "b"):
    print("Бичих хэрэглэгчээ сонго:")
    workers = executeSql("SELECT id, name FROM worker")
    for w in workers:
        print("[%d] %s"%(w[0], w[1]))
    
    w_id = int(input("Хэрэглэгчийн ID: "))
    
    print("Мэдээний ангилал сонго:")
    cats = executeSql("SELECT id, name FROM category")
    for row in cats:
        print("[%d] %s"%(row[0], row[1]))
    
    c_id = int(input("Хэрэглэгчийн ID: "))
    
    title = input("Мэдээний гарчиг: ")
    body = input("Мэдээ: ")

    max_id = executeSql("SELECT MAX(id) FROM content")
    # доорх query-г мөн ашиглаж болно.
    # SELECT IFNULL(0, MAX(id)) FROM content
    if(max_id[0][0] == None):
        new_id = 1
    else:
        new_id = max_id[0][0] + 1

    insertQuery = '''
        INSERT INTO content (id, title, body, worker_id, category_id, created_date) 
        VALUES
        (%d, "%s", "%s", %d, %d, "%s")
    '''%(new_id, title, body, w_id, c_id, datetime.datetime.now())
    
    value = executeSql(insertQuery)

    pass
else:
    print("Буруу сонголт байна. Програм дууслаа.")