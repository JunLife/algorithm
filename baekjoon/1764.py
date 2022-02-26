import sys

n, m = map(int, sys.stdin.readline().split())

cant_listen = list()
cant_see = list()

for i in range(n):
    cant_listen.append(sys.stdin.readline().rstrip())

for i in range(m):
    cant_see.append(sys.stdin.readline().rstrip())

cant_listen.sort()
cant_see.sort()

result = list()

for e in cant_see:
    st = 0
    ed = len(cant_listen) - 1

    while st <= ed:
        mid = (st + ed) // 2

        if cant_listen[mid] == e:
            result.append(e)
            break
        
        if cant_listen[mid] > e:
            ed = mid - 1
        else:
            st = mid + 1

print(len(result))
print('\n'.join(result))