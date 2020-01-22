def func1(st1):
    stack1=Stack(len(st1))
    result=""
    for ch in st1:
        if(ch!="a" and ch!="e" and ch!="i" and ch!="o" and ch!="u"):
            stack1.pop()

        if (ch=="#"):
            stack1.push(ch)

    while(not stack1.is_empty()):
        result+=stack1.pop()
    print result

st = "hi##jack"

func1(st)
