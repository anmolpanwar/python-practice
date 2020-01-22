lst = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
inp1 = 2
inp2 = 7
step = 0
lst1 = [0,0]
def color(input1,input2,lst):
    i=0
    global step
    for i in range(10):
        if lst[input1][i]==1:
            if i==input2:
                step+=1
                break
            else:
                input1=i
                step+=1
                color(input1,input2,lst)
                return None

    print step

color(inp1,inp2,lst)
