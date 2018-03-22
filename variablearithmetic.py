import sys

for line in sys.stdin.readlines():
    line = line.strip()
    if line != '0':
        if '=' in line:
            exec(line)
        else:
            nums = []
            variables = []
            for ele in [str(eval(_)) if _ in locals() else _  for _ in line.split(' + ')]:
                if ele.isdigit():
                    nums.append(int(ele))
                else:
                    variables.append(ele)
            if nums:
                print ' + '.join([str(sum(nums))] + variables)
            else:
                print ' + '.join(variables)
