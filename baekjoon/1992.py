import sys

def d_q(y, x, n, result):
    status = get_status(y, x, n)
    next_n = n // 2
    
    if status != '':
        result += status
        return result
    
    result += '('
    result = d_q(y, x, next_n, result)
    result = d_q(y, x + next_n, next_n, result)
    result = d_q(y + next_n, x, next_n, result)
    result = d_q(y + next_n, x + next_n, next_n, result)
    
    return result + ')'
    
def get_status(y, x, n):
    global board

    pre = board[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if pre != board[i][j]:
                return ''
    
    return str(pre)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    board = [list( map(int, list(sys.stdin.readline().strip())) ) for _ in range(n)]

    result = d_q(0, 0, n, '')
    print(result)