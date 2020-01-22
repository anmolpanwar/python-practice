class A:
    def __init__(self):
        print "parent class init"

    def func1(self):
        print "Parent class func1"

    def func2(self):
        print "Parent class func2"

class B(A):

    def __init__(self):
        obj = A()                       #Super keyword doesn't work in Python 2.7 so we create an object inside function (if we want to call the parent init method)
        print "child class init"

    def func1(self):
        print "Child class func1"



obj = A()
obj2 = B()
obj.func1()                 # dono objects ne apni apni class ka function call kara
obj2.func1()                # doesnt matter if obj2 is object of class B which is inherited from A.
                            #IF METHOD NAME CLASHES IN PARENT AND CHILD, IT CALLS ITS REAL CLASS' METHOD
obj2.func2()

