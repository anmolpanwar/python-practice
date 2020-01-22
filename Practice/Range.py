x = input()
arr = list(map(int, raw_input().split()))
y = int(input())
element = []
for i in range(y):
    element.append(input())

for i in range(y):
    for j in range(len(arr)):
        if arr[j] == element[i]:
            print j+1
