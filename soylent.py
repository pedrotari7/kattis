import sys, math

T = next(sys.stdin)

print '\n'.join([str(int(math.ceil(int(_.strip())/400.))) for _ in sys.stdin])

