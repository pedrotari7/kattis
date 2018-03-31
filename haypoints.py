import sys

m, n = map(int, next(sys.stdin).strip().split())

hay = dict()

for _ in xrange(m):
    line = next(sys.stdin).strip().split()
    hay[line[0].lower()] = int(line[1])

for _ in xrange(n):
    salary = 0
    descrip = ''
    line = next(sys.stdin).strip()
    while line != '.':
        for word in line.split():
            if word in hay:
                salary += hay[word]
        line = next(sys.stdin).strip()

    print salary
