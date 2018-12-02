import sys

solution = {'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3),
            'E': (1, 0), 'F': (1, 1), 'G': (1, 2), 'H': (1, 3),
            'I': (2, 0), 'J': (2, 1), 'K': (2, 2), 'L': (2, 3),
            'M': (3, 0), 'N': (3, 1), 'O': (3, 2), '.': (3, 3)}

print solution

dist = 0

for i, line in enumerate(sys.stdin):
    for j, l in enumerate(line.strip()):
        print solution[l], (i,j), (i-solution[l][0],j-solution[l][1])
