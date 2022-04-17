import sys

n = int(sys.stdin.readline())
values = list()
for _ in range(n):
    values.append(int(sys.stdin.readline()))
    
values.sort()
for v in values:
    print(v)