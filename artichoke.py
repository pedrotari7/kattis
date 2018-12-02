import sys, math

p,a,b,c,d,n = map(int, next(sys.stdin).strip().split())

f = [p*(math.sin(a*k + b) + math.cos(c*k + d) + 2) for k in xrange(1,n+1)]

diff = 0

for i in xrange(len(f)-1):  
    diff = max(diff, f[i] - min(f[i+1:]))

print diff