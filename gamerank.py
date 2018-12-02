import sys

ranks = [0,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,3,3,3,3,3,2,2,2,2,2,2]

rank = 25
stars = 0
streak = 0

for r in list(next(sys.stdin).strip()):
    if r == 'W':
        streak += 1
        stars += 1 + (streak >= 3 and 6 <= rank <= 25) 
        if stars > ranks[rank]:
            stars -= ranks[rank]
            rank -= 1
    elif r == 'L':
        streak = 0
        if stars == 0 and 0 < rank < 20:
            rank += 1
            stars = ranks[rank] - 1
        elif rank <= 19:    
            stars -= 1

print 'Legend' if rank <= 0 else rank