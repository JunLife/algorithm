import sys

n = int(sys.stdin.readline())
value = list()

for i in range(n):
    value.append(int(sys.stdin.readline()))
    
memo = [[0] * 2 for _ in range(max(value) + 1)]
memo[0][0] = 1
memo[0][1] = 0
memo[1][0] = 0
memo[1][1] = 1

for i in range(2, max(value) + 1):
    memo[i][0] = memo[i - 1][0] + memo[i - 2][0]
    memo[i][1] = memo[i - 1][1] + memo[i - 2][1]

for i in value:
    print(memo[i][0], memo[i][1])