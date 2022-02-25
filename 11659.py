import sys

n, m = map(int, sys.stdin.readline().split())
_list = list(map(int, sys.stdin.readline().rstrip().split()))
_sum = [0] * n

for i, v in enumerate(_list):
    if i == 0:
        _sum[i] = v
        continue
    
    _sum[i] = _sum[i - 1] + v
    
result = list()
for _ in range(m):
    st, ed = map(int, sys.stdin.readline().split())
    if st == 1:
        result.append(_sum[ed - 1])
        continue
    result.append(_sum[ed - 1] - _sum[st - 2])

print('\n'.join(map(str, result)))