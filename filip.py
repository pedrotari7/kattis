import sys

print max([int(_[::-1]) for _ in next(sys.stdin).split()])
