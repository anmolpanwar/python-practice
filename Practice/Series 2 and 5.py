def series(len):
    lst = []

    for i in range ((len+1)/2):

        lst.append(2**i)
        lst.append(5**i)

    print "1",               #JUGAAD TO PREVENT 1 from printing twice

    lst.sort()   #optional

    for i in lst:
        if i == lst[0]:
            pass
        else:
            print i,
series(10)

print
print

def series2(num):
    set1={1}                 #values added to set this time, which does not allows any duplicate values

    for i in range((num+1)/2):
        set1.add(2**i)
        set1.add(5**i)

    list1 = []               #then values transferred to list for sorting

    for i in set1:
        list1.append(i)

    list1.sort()

    for i in list1:
        print i,

series2(10)
