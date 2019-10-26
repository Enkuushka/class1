import codecs

# Үг нэмэх
# Үг хайх

dictionary = {}
dictionary["hello"] = "сайн уу"

status = "running"

def addWord(eng, mon):
    #FILE-ruu bichih
    dictFile = codecs.open("dictionary.txt", "a", "utf-8")
    dictFile.write(u'%s--%s\r\n'% (eng, mon))
    dictFile.close()
    # dictionary[eng] = mon
    # print(dictionary)
    

def translate(eng):
    #FILE-aas unshij, haih
    dictFile = codecs.open("dictionary.txt", "r", "utf-8")
    found = False
    translation = "Орчуулга олдсонгүй!"
    while ~found:
        line = dictFile.readline()
        if(line != ""):
            engMon = line.split("--") # list[0] eng, list[1] mon
            if(engMon[0] == eng):
                found = True
                translation = engMon[1]
        else:
            break
    dictFile.close()
    return translation

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