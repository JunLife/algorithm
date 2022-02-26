import sys
from collections import deque

x, k = map(int, sys.stdin.readline().split())
timeline = [float('inf')] * 100001

q = deque()
q.append(x)
timeline[x] = 0

while q:
    now = q.popleft()
    if now == k:
        break
    
    for next in [now - 1, now + 1, now * 2]:
        if 0 <= next < 100001 and timeline[next] == float('inf'):
            q.append(next)
            timeline[next] = timeline[now] + 1
        
print(timeline[k])