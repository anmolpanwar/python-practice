def minimumBribes(n,q):
    bribe = 0
    for i in range(n):
        if (q[i]-(i+1))<3 and (q[i]-(i+1))>=0:
            bribe = bribe + (q[i]-(i+1))
        elif (q[i]-(i+1))>=3:
            print "Too chaotic"
            return
    print bribe


t = int(raw_input())
for _ in xrange(t):
    n = int(raw_input())
    q = map(int, raw_input().rstrip().split())
    minimumBribes(n,q)
