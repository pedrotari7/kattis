import sys

cards = next(sys.stdin)

T = cards.count('T')
C = cards.count('C')
G = cards.count('G')
print T**2 + C**2 + G**2 + 7*min([T, C, G])