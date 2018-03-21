import sys

n = int(next(sys.stdin))

while n != -1:
    n = int(n)
    dist = 0
    prev_time = 0
    for _ in xrange(n):
        speed, time =  map(int,next(sys.stdin).split())
        dist += speed * (time - prev_time)
        prev_time = time
    n = int(next(sys.stdin))

    print dist, 'miles'