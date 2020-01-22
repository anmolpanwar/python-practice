st = raw_input("Enter number: ")

lst = list(st.strip())
dnum=0

for i in range(len(lst)):
    if lst[i]=='A':
        lst[i]=10
    if lst[i]=='B':
        lst[i]=11
    if lst[i]=='C':
        lst[i]=12
    if lst[i]=='D':
        lst[i]=13
    if lst[i]=='E':
        lst[i]=14
    if lst[i]=='F':
        lst[i]=15
    if lst[i]=='G':
        lst[i]=16

lst = [int(i) for i in lst]

for i in range(len(lst)-1,-1,-1):

    dnum = dnum + (17**(len(lst)-i-1))*lst[i]

print dnum
