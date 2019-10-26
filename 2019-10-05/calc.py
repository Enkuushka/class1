# Тооны машин
# - N nemeh
# - H hasah
# - U urjih
# - D huvaah
# - E garah

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mult(a,b):
    return a*b

funcs = {
    "n": add,
    "h": sub,
    "u": mult,
    "d": div
}

isRunning = True

while(isRunning):
    choice = input("enter command (n,h,u,d,e): ")
    if(choice == "e"):
        isRunning = False
    elif(choice in funcs):
        a = float(input("a = "))
        b = float(input("b = "))
        print(funcs[choice](a,b))
    else:
        print("Wrong command!")