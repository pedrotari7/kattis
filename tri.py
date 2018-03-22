from __future__ import division
import sys
from itertools import product

def twolists(list1, list2):
    newlist = []
    a1 = len(list1)
    a2 = len(list2)

    for i in xrange(max(a1, a2)):
        if i < a1:
            newlist.append(list1[i])
        if i < a2:
            newlist.append(list2[i])

    return newlist

operators = ['*','/','+','-','==']

nums = next(sys.stdin).split()

for p in product(operators,operators):
    expression = ''.join(twolists(nums,p))
    if eval(expression) == True and '==' in expression:
        print expression.replace('==','=')
        break

