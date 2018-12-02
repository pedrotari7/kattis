import sys

n = int(next(sys.stdin).strip())

words = next(sys.stdin).strip().split()

output = ['something is fishy', 'makes sense']

print(output[[i+1 if w == 'mumble' else int(w)  for i, w in enumerate(words)] == list(range(1,n+1))])
