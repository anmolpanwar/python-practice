string = raw_input("Enter string: ")

lst = list(string)

n = len(lst)


for i in range(n):

    if lst[i].islower():
        lst[i]='$'

    elif lst[i].isupper():
        lst[i]='&'

string1 = ''.join(lst)

print string1


