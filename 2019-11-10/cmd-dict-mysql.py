import codecs
import mysql.connector

# Үг нэмэх
# Үг хайх

dictionary = {}
dictionary["hello"] = "сайн уу"

status = "running"

mysqlConn = mysql.connector.connect(
    host="localhost",
    user="root",
    database="class_db",
    passwd=""
)

mysqlCursor = mysqlConn.cursor()

def addWord(eng, mon):
    #DATABASE-ruu bichih bolgono
    query = ("INSERT INTO dictionary VALUES (\"%s\", \"%s\")")%(eng, mon)
    mysqlCursor.execute(query)
    

def translate(eng):
    #DATABASE-aas unshij, haih bolgono
    query = ("SELECT mon_word FROM dictionary WHERE eng_word LIKE \"%s\"")%(eng)
    mysqlCursor.execute(query)
    data = mysqlCursor.fetchall()
    if(len(data) == 0):
        return "Үг олдсонгүй."
    return data[0][0]

while(status == "running"):
    print("A - үг нэмэх")
    print("S - үг хайх")
    print("E - гарах")
    choice = input("Та үйлдлээ сонгоно уу: ")

    if(choice == "A" or choice == "a"):
        print("үг нэмэх үйлдэл хийнэ.")
        # ENGLISH MONGOL input
        eng = input("Англи үг: ")
        mon = input("Монгол үг: ")
        # ADD TO DICTIONARY
        addWord(eng, mon)
    elif(choice == "S"):
        # get ENGLISH word
        eng = input("Англи үг бичнэ үү: ")
        # print value in dictionary
        translatedWord = translate(eng)
        print(translatedWord)
    elif(choice == "E"):
        status = "done"
    else:
        print("Буруу комманд!")