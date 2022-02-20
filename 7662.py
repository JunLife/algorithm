import sys, heapq

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    heap = list()
    heap_max = list()
    removed = [None] * 1000001
    
    for j in range(n):
        command, flag = sys.stdin.readline().rstrip().split()
        
        if command == 'I':
            heapq.heappush(heap, (int(flag), j))
            heapq.heappush(heap_max, (-int(flag), j))
            removed[j] = False
            
        elif command == 'D':
            if flag == '-1':
                while heap and removed[heap[0][1]]:
                    heapq.heappop(heap)
                if heap:
                    removed[heap[0][1]] = True
                    heapq.heappop(heap)
            else:
                while heap_max and removed[heap_max[0][1]]:
                    heapq.heappop(heap_max)
                if heap_max:
                    removed[heap_max[0][1]] = True
                    heapq.heappop(heap_max)
    while heap_max and removed[heap_max[0][1]]:
        heapq.heappop(heap_max)
    while heap and removed[heap[0][1]]:
        heapq.heappop(heap)
                    
    if len(heap) == 0:
        print('EMPTY')
    else:
        print(-heap_max[0][0], heap[0][0])