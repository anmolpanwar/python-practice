




list1 = [2,3,4,5,6,7,8,9,12,14,13,54,75,87,345]



evens = list(filter(lambda n : n%2==0, list1)) #filter values using lambda

print evens, "\n"

double_values = list(map(lambda n : n*2, list1)) # do some operations on data values seperately but number of values remain the same

print double_values, "\n"

addition = reduce(lambda a,b : a+b, list1) #do some operation on all and reducing them to a single value

print addition
