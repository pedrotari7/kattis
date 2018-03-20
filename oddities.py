import sys 
n = int(next(sys.stdin))

for _ in xrange(n):
    num = int(next(sys.stdin))
    if num % 2 == 0:
        print str(num) + ' is even'
    else:
        print str(num) + ' is odd'
