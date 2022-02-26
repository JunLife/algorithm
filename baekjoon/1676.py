import sys

n = int(sys.stdin.readline())

result = 1
for i in range(n, 0, -1):
    result *= i

count = 0
target = str(result)
for i in range(len(target) - 1, 0 , -1):
    if target[i] == '0':
        count += 1
        continue
    break
        
print(count)