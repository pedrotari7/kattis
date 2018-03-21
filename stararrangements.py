import sys, math
S = int(next(sys.stdin))

print str(S) + ':'

for i in xrange(2,int(math.ceil(S/2))+2):
    for j in xrange(i-1, i+1):
        if S%(i+j) == 0 or (S-i)%(i+j) == 0:
            print str(i)+','+str(j)