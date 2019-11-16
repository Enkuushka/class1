import mysql.connector
import random

teams = []
counter = 1
game_counter = 1

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

def insertTeam(id, name):
    insertQuery = '''
        INSERT INTO teams (id, name) 
        VALUES
        (%d, "%s")
    '''%(id, name)
    
    value = executeSql(insertQuery)

def insertGame(data):
    global game_counter
    game_counter = game_counter + 1
    insertQuery = '''
        INSERT INTO `games`(`team1_id`, `team2_id`, `team1_pts`, `team2_pts`, `game_date`) 
        VALUES 
        (%d,%d,%d,%d,"%s")
    '''%(data[0],data[1],data[2],data[3],data[4])
    
    value = executeSql(insertQuery)

def getGame():
    team1_id = random.randrange(1, len(teams)+1)
    team2_id = random.randrange(1, len(teams)+1)
    while(team1_id == team2_id):
        team2_id = random.randrange(1, len(teams)+1)

    team1_poins = random.randrange(30, 120)
    team2_poins = random.randrange(30, 120)

    y = 2019
    m = random.randrange(1, 13)
    d = random.randrange(1, 32)
    gamedate = "%d-%d-%d"%(y,m,d)

    return (team1_id, team2_id, team1_poins, team2_poins, gamedate)

aimags = ["Arkhangai", "Bulgan", "Zavkhan", "Gobi-Altai"]
specs = ["Shonkhoruud", "Burgeduud", "Avarguud"]

# Даалгавар: 
# Дээрх aimags, specs-ийн утгуудыг ашиглаад
# Arkhangai burgeduud, Bulgan Avarguud гэх мэт
# нэрсийг үүсгэнэ үү. Бүх боломжоор.

for aimag_ner in aimags:
    for spec_ner in specs:
        teams.append({
            "id" : counter,
            "name" : aimag_ner+" " + spec_ner
        })
        counter = counter + 1

print(teams)
for t in teams:
    insertTeam(t["id"], t["name"])

for i in range(30):
    data = getGame()
    insertGame(data)