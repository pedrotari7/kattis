import sys

s = next(sys.stdin).strip()

w,l,u,symb = 0,0,0,0

for c in s:
    w += c == '_'
    l += c.isalpha() and c == c.lower()
    u += c.isalpha() and c == c.upper()
    symb += not c.isalpha() and c != '_'

total = float(len(s))    

print w / total
print l / total
print u / total
print symb / total

