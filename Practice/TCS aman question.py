string1 = raw_input("Enter: ")

lst = list(string1.strip())
lst = [int(i) for i in lst]

n = len(lst)

odd=0
even=0

for i in range(0,n):
    if i%2!=0:
        even = even + lst[i]
    else:
        odd = odd + lst[i]

print even-odd
