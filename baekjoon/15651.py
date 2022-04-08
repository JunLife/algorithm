from itertools import product
import sys

n, m = map(int, sys.stdin.readline().strip().split())
target = [i for i in range(1, n + 1)]
result = product(target, repeat = m)
for e in result:
    print(' '.join(map(str, e)))