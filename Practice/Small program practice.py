r = list(map(int, raw_input().rstrip().split()))[1]
arr = list(map(int, raw_input().rstrip().split()))
for i in arr[r%len(arr):]:
    print i,
for i in arr[:r%len(arr)]:
    print i,
