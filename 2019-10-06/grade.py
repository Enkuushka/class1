# нийт хүүхдийн тоог авна
# n ширхэг нэр, дүн
# A, B, C, D, F - г оноох
# dictionary ашиглах

# оролт:
# 2
# бат 80
# энх 90

# гаралт:
# бат 80 B
# энх 90 A

table = {}

#INPUT
total = int(input("Нийт оюутны тоо: "))
inputCounter = 0
for i in range(total):
    while inputCounter < total:
        nerDun = input("#"+str(inputCounter)+" Нэр Дүн: ")
        # ner dung salgaj hadgalah
        nerDunList = nerDun.split(" ")
        if(int(nerDunList[1]) <= 100 and int(nerDunList[1]) >= 0):
            table[nerDunList[0]] = {
                "percent": float(nerDunList[1]),
                "symbol": ""
            }
            inputCounter = inputCounter + 1
        else:
            print("Дүн буруу байна. Дахин бичнэ үү.")

#PROCESS
for name in table:
    if(table[name]["percent"] >= 90):
        table[name]["symbol"] = "A"
    elif(table[name]["percent"] >= 80):
        table[name]["symbol"] = "B"
    elif(table[name]["percent"] >= 70):
        table[name]["symbol"] = "C"
    elif(table[name]["percent"] >= 60):
        table[name]["symbol"] = "D"
    else:
        table[name]["symbol"] = "F"
#OUTPUT
for name in table:
    print(name + " " + str(table[name]["percent"]) + " " + str(table[name]["symbol"]))