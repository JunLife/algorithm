import sys
n, m = map(int, sys.stdin.readline().split()) # 나무의 수, 가져갈 나무 길이
trees = list(map(int, sys.stdin.readline().split()))

_min = 0
_max = 2000000000
result = -1
while _min <= _max:
    mid = (_min + _max) // 2
    
    _sum = sum([tree - mid for tree in trees if mid < tree])
    
    if _sum >= m:
        result = mid
        _min = mid + 1
    else:
        _max = mid - 1
    
print(result)