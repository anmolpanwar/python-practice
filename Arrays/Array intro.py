from array import *
# OR import array as arr
vars = array('i',[4,5,6,-2,7,9,2])
#THEN vars=arr.array('i', [....])

print(vars.buffer_info()) # A tuple with 2 entries - address and size
print(vars.append(12))
vars.reverse()
print(vars[0])
print"The type of array is : " , vars.typecode

#ways to print an array

for i in range(8):
    print(vars[i])

print("\n\n\n\n")

for i in range(len(vars)):
    print(vars[i])

print("\n\n\n\n")

for i in vars:
    print(i)

print("\n\n\n")

newarray = array(vars.typecode, (a for a in vars))
# new array defined to copy the vars array
# 2 arguments for defining just like normal array. array(vars.typecode is the type of array for this array and
# a for a in vars - means elements are same as elements in vars...

print(newarray)
print
print
print("FOR LOOP COPY")
#copying array using for loop

for y in vars:
    anotherarray = (vars.typecode, (y for y in vars))

print(anotherarray)

print
print
print

#printing with while loop

x=0







while x<len(vars):
    print(vars[x])
    x+=1
