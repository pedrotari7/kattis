import sys

for v in [map(int, line.split()) for line in sys.stdin]:
    print abs(v[0]-v[1])