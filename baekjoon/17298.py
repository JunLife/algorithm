import sys

n = int(sys.stdin.readline())
_list = list(map(int, sys.stdin.readline().strip().split()))
stack = list()
result = [-1] * n

for i, v in enumerate(_list):
    if not stack:
        stack.append(i)
    else:
        while stack and _list[stack[-1]] < v:
            result[stack.pop()] = v
        stack.append(i)

print(' '.join(map(str, result)))
