def rec(n):
    if(n==1 or n==0):
        return 1
    else:
        n=n*rec(n-1)
    return n
print(rec(7))
