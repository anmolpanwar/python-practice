def fact(n):
    global count
    if n==1:
       return 1
    else:
       count+=1
       lst.append(count)
       return n*fact(n-1)

count = 0
lst = []
print fact(6)
print max(lst)
