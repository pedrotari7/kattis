import sys

s = next(sys.stdin).strip()

l = 1

while 1:
    if len(s) % l == 0:
        valid = True
        for step in xrange(len(s)/l-1):
            if (s[l*step: l*step + l][-1:]+s[l*step: l*step + l][:-1]) != s[l*(step+1): l*(step+1) + l]:
                valid = False
                break
        if valid: break
    l += 1

print l
