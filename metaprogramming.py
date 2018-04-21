import sys

variables = dict()

for command in map(str.strip, sys.stdin):
    command = command.replace('=','==').split()
    if 'define' in command:
        variables[command[2]] = command[1]
    elif 'eval' in command:
        if command[1] not in variables or command[3] not in variables:
            print 'undefined'
        else:
            print str(eval(variables[command[1]]+command[2]+variables[command[3]])).lower()
