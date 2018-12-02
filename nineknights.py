import sys

knights = []

for i,line in enumerate(sys.stdin):
    for j,k in enumerate(line.strip()):
        if k == 'k':
            knights.append((i,j))

print knights

invalid = len(knights) != 9 

for k in knights:
    print 'k', k
    print [(k[0]+1,k[1]+3),(k[0]-1,k[1]+3),(k[0]+1,k[1]-3),(k[0]-1,k[1]-3),(k[0]+3,k[1]+1),(k[0]-3,k[1]+1),(k[0]+3,k[1]-1),(k[0]-3,k[1]-1)]
    if invalid: break
    invalid = ((k[0]+1,k[1]+3) in knights) + ((k[0]+3,k[1]+1) in knights) + \
            ((k[0]-1,k[1]+3) in knights) + ((k[0]-3,k[1]+1) in knights) + \
            ((k[0]+1,k[1]-3) in knights) + ((k[0]-3,k[1]+1) in knights) + \
            ((k[0]-1,k[1]-3) in knights) + ((k[0]-3,k[1]-1) in knights)
print invalid 

if invalid:
    print 'invalid'
else:
    print 'valid'