import sys

N, B = next(sys.stdin).split()

scores = {'A':[11,11],'K':[4,4],'Q':[3,3],'J':[20,2],'T':[10,10],'9':[14,0],'8':[0,0],'7':[0,0]}

score = 0

for line in sys.stdin:
    V, S = list(line.strip())
    score += scores[V][S != B]

print score