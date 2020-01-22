def func1():
    print "demo 2 file func1 " + "name: " + __name__
def func2():
    print "SOME PROGRAM EXECUTED"

def call():
    func1()
    func2()


if __name__ == "demo2":
    print "Error! Execute it from the launcher file not from here"
else:
    print "demo2 executed"
    call()
