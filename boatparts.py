import sys

P, N = map(int, next(sys.stdin).strip().split())

parts = set()

final = 'paradox avoided'

for day, part in enumerate(map(str.strip, sys.stdin)):
    parts.add(part)
    if len(parts) == P:
        final = day + 1
        break

print final
