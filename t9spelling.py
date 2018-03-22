from __future__ import print_function
import sys
n = next(sys.stdin)

k = {' ':0,'a':2,'b':22,'c':222,'d':3,'e':33,'f':333,'g':4,
     'h':44,'i':444,'j':5,'k':55,'l':555,'m':6,'n':66,'o':666,
     'p':7,'q':77,'r':777,'s':7777,'t':8,'u':88,'v':888,'w':9,
     'x':99,'y':999,'z':9999}


for i, text in enumerate(sys.stdin):
    final = [str(k[c]) for c in text.strip('\n')]
    print('Case #{0}: '.format(str(i+1)), end=''),
    prev = '-'
    for key in final:
        if key[0] == prev[0]:
            print(' ' + key, end=''),
        else:
            print(key, end=''),
        prev = key
    print()