import sys
from math import pi

R = int(next(sys.stdin).strip())

euclidian = pi*R**2
taxicab = 2*R**2

print(euclidian)
print(taxicab)