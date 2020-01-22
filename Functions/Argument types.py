#variable length arguements
def function(name, age): #THESE ARE CALLED FORMAL ARGUMENTS
    print "Name:", name
    print "Age:", age

function("Anmol", 21) #THESE ARE *ACTUAL ARGUMENTS*

#FORMAL ARGUMENTS ARE OF 4 TYPES:

#POSITION - Actual arguments given in exact order of Formal arguments. Example above
#DEFAULT - If actual argument(s) not given, default value for that argument(s) is/are mentioned in function declaration.
#VARIABLE LENGTH - Use * to declare variable length of arguments
#KEYWORD - When the actual arguments that can be given by user is not known, we use keyword arguments where we declare the
#          argument values along with their keywords/names. See example

#DEFAULT ARGUMENTS
def function(name, age = 18): #default
    print "Name:", name
    print "Age:", age

function("Anmol")

#VAR LENGTH BY JUGGGGGAAAAAAAAADDDDDDDDDD
def sum(a, b):
    c=a
    print(type(b))

    for i in b:
        c=i+c

    print "Sum:", c

b=[] #LIST CREATED
a=input("Enter first value: ")
b.append(input("Enter next value: ")) #LISTS ARE MUTABLE SO VALUES ARE TAKEN DYNAMICALLY FROM THE USER
i=0
while(b[i]!=0):
    b.append(input("Enter next value: "))
    i+=1

sum(a,b)


#BY DEFAULT THE VALUES PASSED IN ACTUAL VAR LENGTH ARGUMENTS ARE BIND TOGETHER AS 'TUPLE'



#**************************************
#VAR LENGTH ASLI
print
print
print("NOW ORIGINAL VAR LENGTH ARGUMENT COMING UP!!!!!")

def sum2(a, *b):
    c=a
    print(type(b)) #by default b values of b from actual args are formed into a tuple
    print(b)

    for i in b:
        c=i+c

    print "Sum:", c

sum2(12,21,2,32,45)
