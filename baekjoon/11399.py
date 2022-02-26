import sys

n = int(sys.stdin.readline())
_list = list(map(int, sys.stdin.readline().rstrip().split()))

_list.sort()

result = 0
pre = 0
for e in _list:
    result += pre + e
    pre += e

print(result)