from __future__ import division
import sys
from itertools import product, chain
from collections import defaultdict

N = next(sys.stdin)

# v = ['*','+','-','/']

# d = defaultdict(list)

# for p in list(product(v, repeat=3)):
#     expression = ' '.join(chain(*zip(['4']*4, p)))+' 4'
#     r = eval(expression)
#     d[r].append(expression)

# # for n in d:
# for n in map(int, sys.stdin):
#     if n not in d:
#         print 'no solution'
#     else:
#         print d[n][0] + ' = ' + str(n)
# print


possibilities = ['4']

for i in xrange(3):
	ns = []
	for s in possibilities:
		ns.append(s+' * 4')
		ns.append(s+' + 4')
		ns.append(s+' - 4')
		ns.append(s+' / 4')
	possibilities = ns

solutions = {}
for p in possibilities:
	a = eval(p)
	solutions[a] = p


for n in map(int, sys.stdin):
	if n in solutions:
		s = solutions[n]
		print s, '=', n
		#print '4', s[0], '4', s[1], '4', s[2], '4 =', n
	else:
		print('no solution')