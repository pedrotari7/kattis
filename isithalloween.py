import sys

date = next(sys.stdin).strip()


if date in ['DEC 25', 'OCT 31']:
    print('yup')
else:
    print('nope')