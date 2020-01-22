def fac():
    n = input("Enter a number: ")
    fact=n
    for i in range(n-1):
        fact = fact*(n-1)
        n-=1
    print(fact)

fac()
print
print "ALTERNATE METHOD"
print
def fac2():
    n = input("Enter a number: ")
    f=1
    for i in range(1,n+1):
        f=f*i

    return f

factorial=fac2()
print(factorial)
