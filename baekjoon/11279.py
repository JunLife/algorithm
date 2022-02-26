import heapq, sys

n = int(sys.stdin.readline())

heap = list()
for i in range(n):
    value = int(sys.stdin.readline())
    
    if value == 0:
        print_value = 0
        if len(heap) != 0:
            print_value = -heapq.heappop(heap)
        
        print(print_value)
        continue
    
    heapq.heappush(heap, -value)