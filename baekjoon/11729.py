import sys
k = int(sys.stdin.readline())

count = 0
result = list()
def recursion(n, s, t, e):
    global count, result
    count += 1
    
    if n == 1:
        result.append((s, e))
        return
    
    recursion(n - 1, s, e, t)
    result.append((s, e))
    recursion(n - 1, t, s, e)
    
recursion(k, 1, 2, 3)

print(count)
for e in result:
    print(e[0], e[1])