def prime(n):

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


prime(4) #nth prime number
