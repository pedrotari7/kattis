
import sys

class Dog(object):
    def __init__(self, aggressive, calm):
        self.agressive = aggressive
        self.calm = calm

    def is_aggressive(self, time):
        print(time, self.agressive, self.calm, self.agressive + self.calm, time % (self.agressive + self.calm))
        return  0 < (time % (self.agressive + self.calm)) < self.calm


A, B, C, D = map(int, next(sys.stdin).split())

dog1 = Dog(A, B)
dog2 = Dog(C, D)

times = map(int, next(sys.stdin).split())

result = ['none', 'one', 'both']

for t in times:
    print(result[sum([dog1.is_aggressive(t), dog2.is_aggressive(t)])])



