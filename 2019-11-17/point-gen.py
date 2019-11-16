# import mysql.connector
import random

teams = []
counter = 1

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
# TODO: save teams to DB


for i in range(30):
    print(str(i)+" " + str(getGame()))
    # TODO: save to DB