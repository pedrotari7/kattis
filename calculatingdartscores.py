import sys
from itertools import product, combinations_with_replacement, chain
n = int(next(sys.stdin))

c = list(product(range(1, 20+1),range(1, 3+1)))

scores = dict()

for p in list(combinations_with_replacement(c, 1)) + list(combinations_with_replacement(c, 2)) + list(combinations_with_replacement(c, 3)):
    s = sum(_[0]*_[1] for _ in p)
    if s not in scores or len(p) < len(scores[s]):
        scores[s] = p

text = ['single','double','triple']

if n in scores:
    for d in scores[n]:
        print text[d[1]-1], d[0]
else:
    print 'impossible'