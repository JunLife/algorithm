import sys

n = int(sys.stdin.readline())
result =  [0] * (n + 1)
result[0] = 0
result[1] = 1
if n > 1:
    result[2] = 2
        
for i in range(3, n + 1):
    result[i] = result[i - 1] + result[i - 2]
    
print(result[n] % 10007)