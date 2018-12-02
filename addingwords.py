import sys

d = dict()
inv_d = dict()

for line in map(str.strip,sys.stdin):
    if line.startswith('clear'):
        d = dict()
        inv_d = dict()
    elif line.startswith('def'):
        _, key, value = line.split()
        d[key] = value
        inv_d[value] = key
    elif line.startswith('calc'):
        expr = line.split()[1:]
        for i,x in enumerate(expr):
            if x in d:
                expr[i] = d[x]
        try: s = inv_d[str(eval(' '.join(expr[:-1])))]
        except: s = 'unknown'

        print ' '.join(line.split()[1:] + [s])