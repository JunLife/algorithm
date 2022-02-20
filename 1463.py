import sys
n = int(sys.stdin.readline())

dp = [0] * (n + 1)

for i in range(2, 4):
    if i <= n:
        dp[i] = 1
        
for i in range(4, n + 1):
    _list = [dp[i - 1]]
    if i % 3 == 0:
        _list.append(dp[i // 3])
    if i % 2 == 0:
        _list.append(dp[i // 2])
    dp[i] = min(_list) + 1
            
print(dp[n])