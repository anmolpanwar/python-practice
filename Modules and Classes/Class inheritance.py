from math import sqrt

class basic_calc:

    def __init__(self):
        print "Parent class constructor initialized"

    def add(self, num1, *num2):    # VAR LENGTH ARGUMENT

        self.num1 = num1
        self.num2 = num2           # VAR LENGTH ARGUMENT ARE STORED IN FORM OF TUPLES
        sum = num1
        for i in num2:
            sum+=i
        print sum


    def sub(self, big, small):
        self.big = big
        self.small = small

        print self.big - self.small

    sub2 = lambda self, big, small : big - small   # DEFINING SUBTRACT METHOD with the help of lambda

    def div(self, big, small):
        self.big = big
        self.small = small

        print self.big/self.small

    def mul(self, num1, *num2):
        self.num1 = num1
        self.num2 = num2
        product = num1
        for i in num2:
            product = product * i

        print product


class scientific_calc(basic_calc):   #*********INHERITANCE*************

    def __init__(self):                 # IF CHILD CLASS HAS NO CONSTRUCTOR OR INIT METHOD, PARENT INIT IS CALLED AUTOMATICALLY.
        print "child class constructor initialized"

    def root(self, num):
        ans = sqrt(num)

        if ans%1==0:
            print int(ans)
        else:
            print ans

#*****************************************************ATTENTION*******************************************************


    pow = lambda self,num,pow: num**pow  # we can define lambda also in a funtion like this. No need to assign self.num = num  ...bla bla bla... etc. etc.

    display = lambda self, *nums : nums # LAMBDA can also take var length arguments, ek aadha add bhi kar sakte hain par loop nahi chala sakte sare add karne k liye.

op1 = scientific_calc()

op1.root(100)

print op1.pow(3,4) # and call it like a normal method but just we can not print in lambda function directly.


print op1.sub2(35,34)  # LAMBDA function can just return values. Print call karte samay kara lo. Easy.

print op1.display(2,344,1,1,1,232,3) # VAR LENGTH ARGUMENTS FORM A TUPLE AUTOMATICALLY
