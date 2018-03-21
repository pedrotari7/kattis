import sys, math

for line in sys.stdin:
    D,V = map(int,line.split()) 
    if (D,V) != (0,0):
        print ((D**3-(6*V)/math.pi))**(1/3.)