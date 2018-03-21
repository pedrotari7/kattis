import sys

D, M = map(int, next(sys.stdin).split())

d = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30]

w = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

d0 = 3

print w[(d0 + D-1 + sum(d[:M])) % 7]