import sys

def rotate(m):
    s = sum([ord(_) - ord('A') for _ in m])
    return ''.join([chr(((ord(_)-ord('A')) + s) % (ord('Z') - ord('A') + 1)+ord('A')) for _ in m])


m = list(next(sys.stdin).strip())

h = len(m)/2

s1 = rotate(m[:h])
s2 = rotate(m[h:])

final = ''
for c1,c2 in zip(s1,s2):
    final += chr((ord(c1)-ord('A') + ord(c2)-ord('A')) % (ord('Z') - ord('A') + 1) + ord('A'))

print final