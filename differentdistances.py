
import sys

for line in sys.stdin:
    n = map(float, line.strip().split())
    if len(n) > 1:
        point1, point2, p = n[:2], n[2:4], n[-1]
        print (abs(point1[0]-point2[0])**p+abs(point1[1]-point2[1])**p)**(1/p)