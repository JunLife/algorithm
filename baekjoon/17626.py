import sys

n = int(sys.stdin.readline())
result = [None] * (n + 1)
for i in range(3):
    if i < n + 1:
        result[i] = i

for i in range(3, n + 1):
    num = 1
    _min = float('inf')
    
    while num ** 2 <= i:
        _min = min(_min, result[i - num * num])
        num += 1
        
    result[i] = _min + 1

print(result[n])