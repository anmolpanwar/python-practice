from math import sqrt

x = raw_input()
lst = x.split()
m = int(lst[0])
n = int(lst[1])
prime = []
for i in range(m,n+1):
    count = 0
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            count+=1
            break
    else:
        prime.append(i)
sexy = 0
for el in range(len(prime)):
    for k in range(el+1, len(prime)):
        if (prime[el]+6)==prime[k]:
            sexy+=1
            break
print sexy


