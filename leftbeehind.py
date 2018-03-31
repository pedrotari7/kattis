import sys

for line in sys.stdin:
    a, b = map(int, line.strip().split())

    if (a,b) == (0,0): break


    if a+b == 13:
        print 'Never speak again.'
    elif a > b:
        print 'To the convention.'
    elif a < b:
        print 'Left beehind.'
    else:
        print 'Undecided.'

