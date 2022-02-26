n = int(input())
mans = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        if mans[i][0] < mans[j][0] and mans[i][1] < mans[j][1]:
            count += 1
    print(count + 1, end = ' ')