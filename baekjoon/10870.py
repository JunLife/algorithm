import sys

n = int(sys.stdin.readline())

def recursion(n):
    if n == 2 or n == 1 or n == 0:
        return 1
    
    return recursion(n - 1) + recursion(n - 2)

print(recursion(n))