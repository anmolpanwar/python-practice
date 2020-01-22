num = [12,234,5444,44,33,55,19,12,12,23,34,65,10]

for i in num:
    if(i%5==0):
        print(i)
        break
#as soon as 1st multiple of 5 is found, the loop stops. But output stays blank if the number divisible by 5 isn't found.
#so JUST LIKE WE USE ELSE WITH IF, WE HERE USE ELSE WITH FOR

num2 = [12,234,5444,44,33,19,12,12,23,34]
for n in num2:
    if(n%5==0):
        print(n)
        break
    else:
        print("Not found")

#else is repeated because its inside for loop
print("\n\n\n\n\n")
print("New output")

num3 = [55,234,5444,44,33,19,12,12,23,34]
for m in num3:
    if(m%5==0):
        print(m)
        break
else:
        print("Not found")

print "NICE"
