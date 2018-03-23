import sys

pwd, message = map(list, next(sys.stdin).strip().split())

p = True

for c in message:
    if c in pwd:
        if c == pwd[0]:
            pwd.remove(c)
        else:
            p = False

if pwd or not p:
    print 'FAIL'
else:
    print 'PASS'