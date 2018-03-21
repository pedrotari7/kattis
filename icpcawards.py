import sys

N = int(next(sys.stdin))

unis = set()

prizes = 0

for uni, team in map(str.split, sys.stdin):
    if uni not in unis and prizes < 12:
        print uni, team
        unis.add(uni)
        prizes += 1