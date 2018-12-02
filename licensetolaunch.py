import sys

n = next(sys.stdin)

nums = [int(_) for _ in next(sys.stdin).split()]

print(nums.index(min(nums)))
