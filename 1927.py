import heapq
import sys

n = int(sys.stdin.readline())
_list = list()
for i in range(n):
    m = int(sys.stdin.readline())
    
    if m == 0:
        v = 0
        if len(_list) != 0:
            v = heapq.heappop(_list)
        print(v)
        continue

    heapq.heappush(_list, m)