import sys

P = next(sys.stdin)

for line in sys.stdin:
    i, b, K = map(int, line.strip().split())
    ssb = 0
    while K != 0:
        ssb += (K % b)**2
        K = int(K / b )
    print(i, ssb)