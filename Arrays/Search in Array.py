from array import *
arr = array('i', [])

len = input("How many elements?\n")


for i in range(len):
    x=input("Enter element: ")
    arr.append(x)

print(arr)
print

print "now search...\n\n"

el = input("Which element?\n")



for j in range(len):
    if arr[j]==el:
        print "Index number:", j, "(or element number:", j+1,")"
        break
else:
    print "Not found!"

