import sys

nums = sorted(map(int, next(sys.stdin).strip().split()))
order = [ord(o)-ord('A') for o in next(sys.stdin).strip()]

print ' '.join([str(nums[o]) for o in order])