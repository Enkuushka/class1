def add(a, b):
    print(a+b)

def main():
    print("I am main function")
    add(5, 8)

def selfCallingFunc(too):
    if(too > 0):
        print(too)
        selfCallingFunc(too-1)

#selfCallingFunc(4)

## no for, while
## n - from keyboard
## n! = 1*2*3*4...*n
## RECURSIVE FUNCTION example
def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n-1)

#print(factorial(5))



# default value
def printer(text = "Default text"):
    print(text)

#printer("Хэвлүүлэх текст")
#printer()


# олон элемэнттэй аргумент
def listHandler(theList):
    for x in theList:
        print(x)

listHandler([1, "neg", "abc", ("a1",), {"a":1}])

def named(arg1, arg2="default 2"):
    print("arg1 = "+arg1)
    print("arg2 = "+arg2)

#named(arg1 = "neg")


def manyArgs(*args):
    urt = len(args)
    print("Ta "+str(urt)+" ширхэг өгөгдөл дамжуулсан.")
    if(1 in args):
        print("1 baina.")
    #print(args)

manyArgs(1, 2,3, "asdasd", "223")