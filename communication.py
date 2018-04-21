import sys

next(sys.stdin).strip()

for num in [bin(int(_))[2:].zfill(8)[::-1] for _ in next(sys.stdin).strip().split()]:
    prev = 0
    final = ''
    for i in xrange(8):
        n = int(num[i]) ^ prev
        final = str(n) + final
        prev = n

    print int(final, 2),