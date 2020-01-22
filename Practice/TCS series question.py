'''Consider the below series:

1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17

This series is a mixture of 2 series - all the odd terms in this series form a Fibonacci series and all the even terms are the prime numbers in ascending order.

Write a program to find the Nth term in this series'''


from math import sqrt

def fibo(num):
    n=(num+1)/2
    a=1
    b=1
    c=0
    if n==1:
        print "1"
    elif n==2:
        print "1"
    else:
        for i in range(n-2):
            c=a+b
            a=b
            b=c
        print c

def prime(num):
    n=num/2
    plist=[2]
    ln=1
    i=3
    while ln!=n:

        for j in range(2,i):

            if i%j==0:
                break
        else:
            plist.append(i)
            ln+=1

        i+=1

    print plist[n-1]

num1 = input("Enter the element number: ")

if num1%2==0:
    prime(num1)
else:
    fibo(num1)
