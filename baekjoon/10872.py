import sys

def recursion(n):
    if n == 1 or n == 0:
        return 1
    
    return n * recursion(n - 1)

n = int(sys.stdin.readline())

print(recursion(n))