import sys, math

N, W, H =  map(int,next(sys.stdin).split())

for match in map(int, sys.stdin):
    if match <= W or match <= H or match <= math.sqrt(W**2+H**2): 
        print 'DA'
    else:
        print 'NE' 