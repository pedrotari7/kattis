import sys, math

for line in sys.stdin:
    r,m,c = map(float, line.split())
    if (r,m,c) != (0,0,0):
        print math.pi*r**2, 4*r**2*c/float(m)