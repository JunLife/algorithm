import sys

if __name__ == '__main__':
    result = 0
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    target = int(sys.stdin.readline())
    
    nums.sort()
    
    front = 0
    rear = n - 1
    while front < rear:
        _sum = nums[front] + nums[rear]
        if _sum == target:
            result += 1
            rear -= 1
            front += 1
        elif _sum > target:
            rear -= 1
        else:
            front += 1
    print(result)