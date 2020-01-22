lst = list(map(int,raw_input("Enter elements: ").rstrip().split()))
lst.sort()
num = input("Enter search number: ")

def bin(arr,num):
    high = len(arr)-1
    low = 0
    while(low<=high):
        mid = (high+low)/2
        if arr[mid]==num:
            return mid+1
        elif arr[mid]>num:
            high = mid-1
        else:
            low = mid+1
    return "Not found"

print bin(lst,num)
