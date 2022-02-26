import sys, heapq

n = int(sys.stdin.readline())
result = list()
heap = list()

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:
        value = 0
        if heap:
            value = heapq.heappop(heap)[1]
            
        result.append(value)
        continue
    
    heapq.heappush(heap, (abs(x), x))

print('\n'.join(map(str, result)))