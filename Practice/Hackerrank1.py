
lst = list(map(int, raw_input("Enter: ").rstrip().split()))

def simpleArraySum(ar):

    add = reduce(lambda a,b:a+b, ar)
    print add

simpleArraySum(lst)
