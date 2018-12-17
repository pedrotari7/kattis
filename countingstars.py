import sys
i = 0
while 1:
    i+=1
    try:
        R, C = map(int,next(sys.stdin).strip().split())
    except:
        break

    sky = {(r,c): s for r in xrange(R) for c, s in enumerate(list(next(sys.stdin).strip())) if s == '-'}

    not_visited = sky.keys()

    count = 0
    while not_visited:
        count += 1
        s = not_visited.pop()
        galaxy = set([s])
        seen = set([s])
        while galaxy:
            p = galaxy.pop()
            for u in [(p[0]+1,p[1]),(p[0]-1,p[1]),(p[0],p[1]+1),(p[0],p[1]-1)]:
                if u in sky and u not in seen:
                    seen.add(u)
                    if u in not_visited:
                        not_visited.remove(u)
                    if u not in galaxy:
                        galaxy.add(u)

    print 'Case '+ str(i)+ ': ' + str(count)