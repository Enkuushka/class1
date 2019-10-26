# Үг нэмэх
# Үг хайх

dictionary = {}
dictionary["hello"] = "сайн уу"

status = "running"

def addWord(eng, mon):
    dictionary[eng] = mon
    print(dictionary)

def translate(eng):
    if(eng in dictionary):
        return dictionary[eng]
    else:
        return "Орчуулга олдсонгүй!"

while (status == "running"):
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