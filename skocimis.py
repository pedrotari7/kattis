import sys

A, B, C = map(int, next(sys.stdin).strip().split())

print max(abs(A-B), abs(C-B)) - 1 
