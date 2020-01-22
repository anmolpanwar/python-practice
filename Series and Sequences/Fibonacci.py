def fibonacci():
    a = 0
    b = 1
    n=input("Enter the lenth of series: ")
    if (n==1):
        print a
    elif(n==0):
        print "Fuck off!"
    else:
        print a
        print b
        for i in range(n-2):
            sum = a+b
            a=b
            b=sum
            print(sum)

fibonacci()
