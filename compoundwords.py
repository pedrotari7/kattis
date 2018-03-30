import sys, itertools

words = sum([line.strip().split() for line in sys.stdin], [])

print '\n'.join(sorted(set([''.join(_) for _ in  itertools.permutations(words, 2)])))