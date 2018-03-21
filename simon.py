import sys
n = int(next(sys.stdin))

for line in sys.stdin:
    m = line.split('simon says ')
    if len(m) > 1:
        print m[1].strip()
    else:
        print