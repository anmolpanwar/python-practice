lst = [[1,43,53],[12,45,65],[24,54,5]]

for i in range(len(lst)):
    for j in range(len(lst[0])):
        try:
            if lst[i+1][j+1]:
                print(lst[i+1])
        except:
            pass
