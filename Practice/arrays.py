arr = []

for _ in range(6):
    arr.append(map(int, raw_input().rstrip().split()))

sum = 0
lst = []

for i in range(4):
    for j in range(4):
        sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        lst.append(sum)

lst.sort()

print lst[15]
