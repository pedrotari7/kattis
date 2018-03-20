import sys, math

h, v = map(int, next(sys.stdin).split())

print int(math.ceil(h/math.sin(math.radians(v))))