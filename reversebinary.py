import sys
print int(''.join(reversed(bin(int(next(sys.stdin)))[2:])),2)
