def add(x,y):
    print x+y

def newadd(func):
    def inner(x,y):
        print x*y

    inner(x,y)

newadd(add(3,2))


