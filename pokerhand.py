import sys
from collections import Counter

hand = map(lambda x: x[0], next(sys.stdin).strip().split())

print(Counter(hand).most_common(1)[0][1])
