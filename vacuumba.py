import sys
from math import cos, sin, radians

n = int(next(sys.stdin).strip())

for i in range(n):

    m = int(next(sys.stdin).strip())

    current_theta, x, y = 90, 0, 0


    for j in range(m):
        theta, d = map(float, next(sys.stdin).strip().split())

        current_theta += theta

        x += d*cos(radians(current_theta))
        y += d*sin(radians(current_theta))

    print('%.8f %.8f' % (x,y))


