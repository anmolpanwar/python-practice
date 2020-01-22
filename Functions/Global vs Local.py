a=10                        #GLOBAL declaration

def function():
    a=5                     #LOCAL declararation
    print "Local a:", a
    b=8                     #LOCAL declararation
    print "Local b:",b

print "Global a:",a

function()

def function2():

    global a
    a=100

    print "In function:", a


function2()
print "outside:", a

