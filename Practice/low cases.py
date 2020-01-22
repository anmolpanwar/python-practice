#METHOD - 1 (Ordinary)

def check(start,end,num):
    if num>start and num<end:
        return True
    else:
        return False

start = input("enter start: ")
end = input("enter end: ")
num = input("enter num: ")

print check(start,end,num)


#METHOD - 2 (Shorter)

def check2(start,end,num):
    return num>start and num<end    #if me yahi condition likhte, true hoti to andar ka code chal jata. Iss case me bhi agar
                                    #condition true hui to true return ho jaega, false hui to false return ho jaega

print(check2(input("Enter start: "), input("Enter end: "), input("Enter number: ")))


# METHOD - 3 (Shortest)

check3 = lambda s,e,n : (n<e and n>s)

print check3(input("Enter: "), input("Enter: "), input("Enter: "))

# PYTHON me direct argument me hi input le sakte hain
