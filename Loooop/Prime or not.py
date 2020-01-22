import math
x=input("Gimme something man: ")
sq = int(math.sqrt(x))
for i in range(2, sq+1):
    if(x%i==0):
        print("NOT PRIME")
        break
else:
    print("OPTIMUS PRIME")
