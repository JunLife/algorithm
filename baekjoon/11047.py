import sys
n, k = map(int, sys.stdin.readline().strip().split())

coins = list()
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

count = 0
now = 0
for i in range(len(coins) - 1, -1, -1):
    if k == now:
        break
    
    if k - now >= coins[i]:
        num = (k - now) // coins[i]
        count += num
        now += coins[i] * num

print(count)