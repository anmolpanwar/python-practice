def xseries(string):

    arr = list(string.split(","))

    num = []

    for i in arr:
        i = int(i)
        num.append(i)

    n = len(num)
    subl = []
    m=1
    for i in range(n-2):

        if num[i]+num[i+1]==num[i+2]:
            subl.append(num[i])
            subl.append(num[i+1])
            subl.append(num[i+2])


            while (subl[m]+subl[m+1]!=num[i+m+2]):
                subl.append(num[i+3])
                m+=1

        else:
            pass
    if len(subl)==0:
        print "-1"

inputstring = raw_input("Enter: ")
xseries(inputstring)

