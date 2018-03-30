import sys

final = []

for n in next(sys.stdin):
    if n != '<': final.append(n)
    elif final: final.pop()

print ''.join(final)