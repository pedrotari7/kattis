import sys
from math import cos, tan, radians
N = int(next(sys.stdin))

for _ in xrange(N):
    v0, theta, x1, h1, h2 = map(float, next(sys.stdin).split())

    theta = radians(theta)

    t = x1 / float(v0 * cos(theta))

    y = tan(theta) * x1 - 0.5*9.81*t**2

    if h1+1 <= y <= h2-1:
        print 'Safe'
    else:
        print 'Not Safe'