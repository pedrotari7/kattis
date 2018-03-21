import sys

m = next(sys.stdin)

for p in ['a','e','i','o','u']:
    m = m.replace(p+'p'+p,p)
print m