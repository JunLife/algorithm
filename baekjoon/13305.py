import sys

n = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().strip().split()))
price = list(map(int, sys.stdin.readline().strip().split()))

min_price = price[0]
result = dis[0] * min_price
for i in range(1, n - 1):
    if min_price >= price[i]:
        min_price = price[i]
    result += min_price * dis[i]
    
print(result)