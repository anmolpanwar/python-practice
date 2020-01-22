def reverse(num):
    temp=num
    rev=0
    while(temp>0):
        dig = temp%10
        rev = rev*10 + dig
        temp/=10

    return rev
def pal(sum):
    temp=sum
    rev=0
    while(temp>0):
        dig = temp%10
        rev = rev*10 + dig
        temp/=10

    if (rev==sum):
        print rev
    else:
        return False


number = input()
revnum = reverse(number)

sum = number+revnum
pal(sum)

