import sys
expression = sys.stdin.readline()
expression = expression.replace('\n', '')

tmp = ''
values = []
for i, v in enumerate(expression):
    if v == '+':
        values.append(int(tmp))
        tmp = ''
        continue
    if v == '-':
        values.append(int(tmp))
        values.append(v)
        tmp = ''
        continue
    
    tmp += v    
values.append(int(tmp))

tmp = 0
result = 0
flag = False
for i in range(len(values) - 1, -1, -1):
    if values[i] == '-':
        result -= tmp
        tmp = 0
        flag = True
        continue
    
    tmp += values[i]
    
result += tmp
print(result)