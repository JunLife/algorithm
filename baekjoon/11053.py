import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(max(dp))