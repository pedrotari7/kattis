import sys
from collections import defaultdict

votes = defaultdict(int)

for name in map(str.strip, sys.stdin):
    if name != '***':
        votes[name] += 1

sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)

if len(sorted_votes) == 1 or (len(sorted_votes) > 1 and sorted_votes[0][1] > sorted_votes[1][1]):
    print sorted_votes[0][0]
else:
    print 'Runoff!'