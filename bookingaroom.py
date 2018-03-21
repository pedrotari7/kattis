import sys

r, n = map(int,next(sys.stdin).strip().split())

rooms = set()

if n > 0:
    for room in sys.stdin:
        rooms.add(int(room))

if n == r:
    print 'too late'
else:
    s = set(range(1,r+1))
    free_rooms = s-rooms
    print free_rooms.pop()

