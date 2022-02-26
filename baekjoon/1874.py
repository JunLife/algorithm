import sys
from collections import deque

result = ''
n = int(sys.stdin.readline())
order = deque()
for _ in range(n):
    order.append(int(sys.stdin.readline()))

stack = list()
for i in range(1, n + 1):
    while stack and stack[-1] == order[0]:
        result += '-'
        stack.pop()
        order.popleft()
        continue
    result += '+'
    stack.append(i)
    
for e in order:
    if e == stack[-1]:
        result += '-'
        stack.pop()
        continue
    result = 'NO'
    break

if result == 'NO':
    print(result)
else:
    for e in result:
        print(e)