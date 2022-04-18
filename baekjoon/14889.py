import sys

def dfs(level, now, st_index):
    global result
    
    if level >= team_n:
        team1 = team2 = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if check[i] and check[j]:
                    team1 += matrix[i][j]
                elif not check[i] and not check[j]:
                    team2 += matrix[i][j]
                    
        result = min(result, abs(team1 - team2))
        return
    
    for i in range(st_index, n):
        if check[i]:
            continue
        
        check[i] = True
        now.append(i + 1)
        dfs(level + 1, now, i)
        now.pop()
        check[i] = False

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    check = [False] * n
    matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

    team_n = n // 2
    result = float('inf')
    check[0] = True
    dfs(1, [1], 1)
    print(result)