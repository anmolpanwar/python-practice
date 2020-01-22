''' Given a series whose even term creates a separate geometric series and odd term creates another geometric series. Write a program to generate such series.
    For example:
    Input:

    Enter the number of terms : 10
    Enter the common ratio for G.P - 1 : 2
    Enter the common ratio for G.P - 2 : 3

    Output:

    The series is
    1  1  2  3  4  9  8  27  16  81
'''

def geo1(ratio,terms):
    n = (terms+1)//2                #this list prints its elements first, so in case of odd numbers, iska ek element zyda rahega geo2 se
    lst=[]                          #total elements = 11; geo1 elements = 6; and geo2 elements = 5
    itr = 0
    a=1
    while itr!=n:

        lst.append(a)
        a=a*ratio
        itr+=1

    return lst

def geo2(ratio2,terms2):
    n2 = (terms2)//2                #an element less is printed in case of total odd terms
    lst2=[]                         #in case of even, SAME!
    itr2 = 0
    a2=1
    while itr2!=n2:

        lst2.append(a2)
        a2=a2*ratio2
        itr2+=1
    return lst2

terms = input("Enter number of terms: ")
gr = input("Enter ratio for 1st GP: ")
gr2 = input("Enter ratio for 2nd GP: ")

gp = geo1(gr,terms)
gp2 = geo2(gr2,terms)

try:                                    #odd number me gp2 me ek term kam hoti hai than gp. so last iteration of for loop causes a 'list index out of bounds error'
    for i in range((terms+1)/2):        #so put this in try block and except the error, the program excepts the error and terminates normally
        print gp[i],
        print gp2[i],
except:
    pass
