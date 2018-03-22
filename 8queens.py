import sys

queens = []
for i,line in enumerate(sys.stdin):
    for j, p in enumerate(line):
        if p == '*':
            queens.append((i,j))

valid = True if len(queens) == 8 else False

if valid:
    for i,j in queens:
        if not valid:
            break
        for a,b in queens:
            if (i,j) == (a,b): continue
            if i == a or j == b or i+j==a+b or ((a-b) == (i-j)):
                valid = False

if valid:
    print 'valid'
else:
    print 'invalid'