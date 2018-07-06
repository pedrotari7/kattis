import sys

current_player = int(next(sys.stdin).strip())

N = next(sys.stdin)

time_remaining = 60*3+30

for T, Z in map(lambda x: (int(x[0]),x[1]), map(str.split, sys.stdin)):

    time_remaining -= T

    if time_remaining <= 0: break

    if Z == 'T':
        current_player = (current_player % 8) + 1


print(current_player)