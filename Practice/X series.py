c = map(int, raw_input().rstrip().strip())
jump,i = 0,0

while i<len(c)-2:
    if c[i+2]==0 or c[i+1]==1:
        jump+=1
        i+=2
    elif c[i+2]==1 or c[i+1]==0:
        jump+=1
        i+=1

print jump
