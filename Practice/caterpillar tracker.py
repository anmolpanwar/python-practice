l,garden,count,i,a,b,nstep = [],[],0,0,0,1,0

l.append(raw_input())

while l[i]!='x':
    l.append(raw_input())
    i+=1

for i in range(len(l)-1):
    l[i] = l[i].rstrip().split()
    l[i][0] = int(l[i][0])

l.remove('x')

nindex = 0

for i in range(len(l)):
    if l[i][1]=='NE' or l[i][1]=='N' or l[i][1]=='NW':
        nindex = i
        break

for i in range(len(l)):
    if i<nindex:
        if l[i][1]=='SE' or l[i][1]=='S' or l[i][1]=='SW':
            count+=l[i][0]
    else:
        if l[i][1]=='SE' or l[i][1]=='S' or l[i][1]=='SW':
            nstep+=l[i][0]
        elif l[i][1]=='NE' or l[i][1]=='N' or l[i][1]=='NW':
            nstep-=l[i][0]

if nstep>0:
    count+=nstep
else:
    pass

for i in range(count+1):
    garden.append(['|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|'])

if len(l)==0:
    garden[0][1]='x'

for i in range(len(l)):
    for j in range(l[i][0]):

        if l[i][1]=="E":
            garden[a][b] = "-"
            b+=1

        elif l[i][1]=="N":
            garden[a][b] = "|"
            a-=1

        elif l[i][1]=="NE":
           garden[a][b] = "/"
           a-=1
           b+=1

        elif l[i][1]=="NW":
            garden[a][b] = "\\"
            a-=1
            b-=1

        elif l[i][1]=="W":
            garden[a][b] = "-"
            b-=1

        elif l[i][1]=="SE":
            garden[a][b] = "\\"
            a+=1
            b+=1

        elif l[i][1]=="S":
            garden[a][b] = "|"
            a+=1

        elif l[i][1]=="SW":
            garden[a][b] = "/"
            a+=1
            b-=1

    garden[a][b]= "x"


for i in range(len(garden)):
    for j in range(12):
        print garden[i][j],
    print
