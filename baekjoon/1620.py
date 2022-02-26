import sys

n, m = map(int, sys.stdin.readline().split())

_dic = dict()
for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    _dic[name] = i
    _dic[str(i)] = name
    
result = list()
for i in range(m):
    target = sys.stdin.readline().rstrip()
    
    result.append(str(_dic[target]))
    
print('\n'.join(result))