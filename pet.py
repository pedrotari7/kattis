import sys
grades = [sum(map(int, line.strip().split())) for line in sys.stdin]

print grades.index(max(grades))+1, max(grades)