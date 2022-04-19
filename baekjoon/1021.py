import sys
from collections import deque

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split()) # 큐의 길이, 뽑아내는 수의 개수
    nums = deque(list(map(int, sys.stdin.readline().strip().split()))) # 뽑아내는 수의 위치
    count = 0
    _list = list()
    
    for i in range(1, n + 1):
        _list.append(i)
    
    q = deque(_list)
    
    while nums:
        if q[0] == nums[0]:
            nums.popleft()
            q.popleft()
            continue
        
        count += 1
        if q.index(nums[0]) <= len(q) // 2:
            q.rotate(-1)
        else:
            q.rotate(1)
    
    print(count)