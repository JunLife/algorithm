import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

pn = 'I' + 'OI' * n

count = 0
result = 0
i = 0
while i < m:
    if s[i:i + 3] == 'IOI':
        i += 2
        count += 1
        if count == n:
            count -= 1
            result += 1
            
        if i + 3 >= m:
            break
    else:
        i += 1
        count = 0
            
print(result)