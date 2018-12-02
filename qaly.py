import sys

N = next(sys.stdin)

qaly = 0

for line in sys.stdin:
    qa = list(map(float,line.strip().split()))
    qaly += qa[0]*qa[1]

print(qaly)
