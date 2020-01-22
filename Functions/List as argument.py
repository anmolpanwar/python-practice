def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd #Return in python can return more than 1 value...

lst=[12,23,324,54,56,32,76,236,76,23,45,67,78]

even,odd = count(lst) #these values are assigned to 2 variables outside function is same order

print
print "IMPORTANT THING"
#WAYS TO PRINT THE SAME THING

print "Method 1"
print "Odd count:",odd
print "Even count:", even

print "Method 2"
print "Even: {} and Odd: {}".format(even, odd)

